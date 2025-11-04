import subprocess, os

# def snake_to_pascal(snake_str: str) -> str:
#     return ''.join(word.capitalize() for word in snake_str.split('_'))

def paths_from_input():
    import argparse

    parser = argparse.ArgumentParser(description="Inserisci immagini/snippet e converti in DOCX.")
    parser.add_argument("file", help="Nome del file markdown")

    input_file = parser.parse_args().file

    if not os.path.splitext(input_file)[1]:
        input_file += ".md"

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    title_case = base_name.capitalize()

    # title_case = snake_to_pascal(base_name)

    default_input = os.path.join("", title_case, base_name + os.path.splitext(input_file)[1])
    if not os.path.exists(default_input):
        raise FileNotFoundError(f"File non trovato: {default_input}")

    return (
        default_input,
        base_name,
        os.path.join("", title_case, "immagini"),
        os.path.join("", title_case, "snippets"),
        os.path.join("", title_case, f"{base_name}_output")
    )

def puml_to_svg():
    input_path, base_name, image_dir, code_dir, output_dir = paths_from_input()

    extra_snippet_dir = os.path.join(code_dir, "extra")

    print("🧩 Generazione immagini da file .puml in corso...")
    puml_root_dirs = [d for d in [code_dir, extra_snippet_dir] if not d.startswith(os.path.join(code_dir, "extra"))]
    svg_count = 0
    for search_dir in puml_root_dirs:
        if os.path.isdir(search_dir):
            for root, _, files in os.walk(search_dir):
                for f in files:
                    if f.lower().endswith(".puml"):
                        puml_path = os.path.join(root, f)
                        rel_subdir = os.path.relpath(root, code_dir)
                        svg_dir = os.path.join(image_dir, rel_subdir)
                        os.makedirs(svg_dir, exist_ok=True)
                        svg_name = os.path.splitext(f)[0] + ".svg"
                        svg_path = os.path.join(svg_dir, svg_name)
                        if process_puml(puml_path, svg_path):
                            svg_count += 1

    print(f"Generati {svg_count} diagrammi UML.\n")
    return input_path, base_name, image_dir, code_dir, output_dir, extra_snippet_dir

def process_puml(puml_path, svg_path, max_retries=5, retry_delay=2):
    from plantuml import PlantUML, PlantUMLHTTPError
    import time
    server = PlantUML(url='http://www.plantuml.com/plantuml/svg/')

    os.makedirs(os.path.dirname(svg_path), exist_ok=True)

    for attempt in range(1, max_retries + 1):
        try:
            result = server.processes_file(puml_path, outfile=svg_path)
            if result:
                print(f"✅ {svg_path} generato!")
                return True
            else:
                print(f"⚠️ {puml_path} non è stato generato correttamente")
                return False

        except PlantUMLHTTPError as e:
            print(f"⚠️ Errore PlantUMLHTTPError ({type(e).__name__}) con {os.path.basename(puml_path)} "
                  f"al tentativo {attempt}/{max_retries}: {str(e)}")
            if attempt < max_retries:
                time.sleep(retry_delay)
                print("↻ Riprovo...")
            else:
                print(f"❌ Falliti tutti i tentativi per {os.path.basename(puml_path)}")
                return False

        except Exception as e:
            msg = str(e)
            print(f"⚠️ Errore generico con {os.path.basename(puml_path)}: {msg} "
                  f"(tentativo {attempt}/{max_retries})")

            if "PlantUMLHTTPError" in msg or "HTTP" in msg:
                if attempt < max_retries:
                    time.sleep(retry_delay)
                    print("↻ Riprovo...")
                    continue
                else:
                    print(f"❌ Falliti tutti i tentativi per {os.path.basename(puml_path)}")
                    return False
            else:
                return False
    return None

def __init__():
    puml_to_svg()