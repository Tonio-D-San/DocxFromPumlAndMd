import os
import pypandoc
import shutil
from subprocess import run, CalledProcessError

from . import managepuml

from . import installpackages

SUPPORTED_CODE_EXT = [".puml", ".py", ".java", ".js", ".txt"]

yes_no = installpackages.install_missing_packages()

def ensure_png(image_path):
    if not image_path.lower().endswith(".svg"):
        return image_path

    png_path = os.path.splitext(image_path)[0] + ".png"
    if os.path.exists(png_path):
        return png_path

    rsvg = shutil.which("rsvg-convert")
    inkscape = shutil.which("inkscape")
    for tool in [(rsvg, [rsvg, "-o", png_path, image_path]),
                 (inkscape, [inkscape, image_path, "--export-type=png", "--export-filename", png_path])]:
        if tool[0]:
            try:
                run(tool[1], check=True)
                return png_path
            except CalledProcessError:
                pass

    print(f"⚠️ Non ho potuto convertire {image_path} in PNG (manca rsvg-convert/inkscape).")
    return image_path

def md_from_input(input_path):
    ext = input_path.lower().split(".")[-1]
    if ext == "md":
        with open(input_path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == "docx":
        return pypandoc.convert_file(input_path, "markdown_github")
    else:
        raise ValueError("Input file must be .md or .docx")

def add_extra_media(text, extra_image_dir, extra_snippet_dir, supported_ext=None):
    supported_ext = supported_ext or SUPPORTED_CODE_EXT
    if os.path.isdir(extra_image_dir):
        extra_imgs = [f for f in os.listdir(extra_image_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".svg"))]
        if extra_imgs:
            text += "\n\n---\n\n# Diagrammi aggiuntivi\n\n"
            for img in extra_imgs:
                img_path = os.path.join(extra_image_dir, img)
                if yes_no:
                    img_path = ensure_png(img_path)

                text += f"![{os.path.splitext(img)[0]}]({img_path})\n\n"

                snippet_path = None
                if os.path.isdir(extra_snippet_dir):
                    base_img_name = os.path.splitext(img)[0].lower()
                    for f in os.listdir(extra_snippet_dir):
                        if f.lower().startswith(base_img_name):
                            ext = os.path.splitext(f)[1].lower()
                            if ext in supported_ext:
                                snippet_path = os.path.join(extra_snippet_dir, f)
                                break
                if snippet_path:
                    ext = os.path.splitext(snippet_path)[1].lstrip(".")
                    try:
                        with open(snippet_path, "r", encoding="utf-8") as sf:
                            snippet_text = sf.read()
                    except Exception as e:
                        snippet_text = f"# Errore nella lettura del file: {e}"
                    text += f"```{ext}\n{snippet_text}\n```\n"
            print(f"🖼️  Aggiunte {len(extra_imgs)} immagini extra e relativi snippet")
    return text

def insert_media(text, image_dir, code_dir, supported_ext=None):
    import re
    from . import utils
    supported_ext = supported_ext or SUPPORTED_CODE_EXT
    section_pattern = re.compile(
        r"(##\s*(?:\*\*)?(?P<title>.*?)(?:\*\*)?\s*\n)(?P<body>.*?)(?=(\n##\s|\Z))", re.S | re.M
    )

    def replacement(match):
        heading_line = match.group(1)
        title = match.group("title").strip()
        body = match.group("body")
        slug = utils.normalize_endpoint(title)
        insert_block = ""

        img_found = None
        if os.path.isdir(image_dir):
            for f in os.listdir(image_dir):
                if f.lower().startswith(slug) and f.lower().endswith((".png", ".jpg", ".jpeg", ".svg")):
                    img_found = os.path.join(image_dir, f)
                    break
        if img_found:
            img_to_use = img_found
            if yes_no:
                img_to_use = ensure_png(img_found)
            rel_img = os.path.relpath(img_to_use)
            insert_block += f"\n\n![Diagramma {title}]({rel_img})\n"

        code_found = None
        if os.path.isdir(code_dir):
            for f in os.listdir(code_dir):
                if f.lower().startswith(slug):
                    ext = os.path.splitext(f)[1].lower()
                    if ext in supported_ext:
                        code_found = os.path.join(code_dir, f)
                        break
        if code_found:
            ext = os.path.splitext(code_found)[1].lstrip(".")
            try:
                with open(code_found, "r", encoding="utf-8") as cf:
                    code_text = cf.read()
            except Exception as e:
                code_text = f"# Errore nella lettura del file: {e}"
            insert_block += f"\n```{ext}\n{code_text}\n```\n"

        new_section = heading_line + body
        if insert_block and insert_block.strip() not in new_section:
            new_section = new_section.rstrip() + "\n\n" + insert_block + "\n"
        return new_section

    return section_pattern.sub(replacement, text)

def write_and_convert():
    input_path, base_name, image_dir, code_dir, output_dir, extra_snippet_dir = managepuml.puml_to_svg()
    md_text = add_extra_media(
        insert_media(
            md_from_input(input_path),
            image_dir,
            code_dir
        ),
        os.path.join(image_dir, "extra"),
        extra_snippet_dir
    )
    os.makedirs(output_dir, exist_ok=True)
    out_md = os.path.join(output_dir, f"{base_name}_documentation.md")
    out_docx = os.path.join(output_dir, f"{base_name}_documentation.docx")

    with open(out_md, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"Markdown arricchito scritto in: {out_md}")

    pypandoc.convert_file(out_md, "docx", outputfile=out_docx, format="md", extra_args=["--standalone"])
    print(f"DOCX generato: {out_docx}")
    return out_md, out_docx

def __init__():
    write_and_convert()