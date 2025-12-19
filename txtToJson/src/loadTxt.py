import argparse
import os
import json

from dotenv import load_dotenv

def load_and_convert():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Importa tabelle md in Excel formattato.")
    parser.add_argument("--type", help="Indicare se si tratta di pod o pdr")
    parser.add_argument("--input", help="Nome file txt senza estensione")
    parser.add_argument("--output", help="Nome file json senza estensione")
    args = parser.parse_args()

    pod_or_pdr = args.type if args.type else os.getenv("TYPE")
    txt_file = f"{args.input if args.input else os.getenv("TXT_FILE")}.txt"
    json_base = f"{args.output if args.output else os.getenv("JSON_FILE")}"

    json_file = f"{json_base}_{pod_or_pdr}.json"

    print(f"Leggo: {txt_file}")

    data_inizio_estrazione = "2023-10-01"

    with open(txt_file, "r", encoding="utf-8") as f:
        pod_list = [line.strip() for line in f if line.strip()]

    data = {
        "richieste": [
            {pod_or_pdr: pod, "dataInizioEstrazione": data_inizio_estrazione}
            for pod in pod_list
        ]
    }

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"File JSON generato correttamente: {json_file}")