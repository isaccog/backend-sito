
import os
import json
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key="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")

# Configura API os.getenv("OPENAI_API_KEY")
LANGUAGES = {"en": "English", "fr": "French"}

def traduci_testo(testo, lang_codice):
    lang_nome = {"en": "inglese", "fr": "francese"}[lang_codice]
    prompt = f"Traduci in {lang_nome}, mantieni i tag HTML se presenti ma non tradurre le chiavi 'testo', 'titolo' e 'pubblicazione':\n\n{testo}"
    response = client.chat.completions.create(model="gpt-4",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()

def traduci_articolo_txt(file_path):
    with open(file_path, encoding="utf-8") as f:
        contenuto = f.read()
    for lang in LANGUAGES:
        dest = file_path.with_stem(file_path.stem + f"_{lang}")
        if dest.exists():
            continue
        print(f"✏️ Traduco {file_path.name} → {dest.name}")
        tradotto = traduci_testo(contenuto, lang)
        with open(dest, "w", encoding="utf-8") as out:
            out.write(tradotto)

def traduci_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        dati = json.load(f)
    for lang in LANGUAGES:
        dest = file_path.with_stem(file_path.stem + f"_{lang}")
        if dest.exists():
            continue
        print(f"✏️ Traduco {file_path.name} → {dest.name}")
        if isinstance(dati, list):
            tradotti = []
            for item in dati:
                item_copy = item.copy()
                for k in ["description", "descrizione", "testo", "titolo"]:
                    if k in item:
                        item_copy[k] = traduci_testo(item[k], lang)
                tradotti.append(item_copy)
        else:
            tradotti = dati
        with open(dest, "w", encoding="utf-8") as out:
            json.dump(tradotti, out, ensure_ascii=False, indent=2)

def main():
    for file in Path("articoli").glob("*.txt"):
        traduci_articolo_txt(file)
    for file in Path("data").glob("*.json"):
        traduci_json(file)

if __name__ == "__main__":
    main()
