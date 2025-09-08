import json
import os
from pathlib import Path
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LANGUAGES = {"en": "English", "fr": "French"}
CACHE_PATH = Path(".translation_cache.json")

def load_cache():
    if CACHE_PATH.exists():
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def is_updated(file_path: Path, lang: str, cache: dict):
    file_key = str(file_path)
    file_mtime = file_path.stat().st_mtime

    if file_key not in cache:
        return True
    if lang not in cache[file_key].get("langs", []):
        return True
    return file_mtime > cache[file_key]["last_modified"]

def update_cache(file_path: Path, lang: str, cache: dict):
    file_key = str(file_path)
    file_mtime = file_path.stat().st_mtime
    if file_key not in cache:
        cache[file_key] = {"langs": [lang], "last_modified": file_mtime}
    else:
        cache[file_key]["last_modified"] = file_mtime
        if lang not in cache[file_key]["langs"]:
            cache[file_key]["langs"].append(lang)

def traduci_testo(testo, lang_codice):
    lang_nome = {"en": "inglese", "fr": "francese"}[lang_codice]
    prompt = f"Traduci in {lang_nome}, mantieni i tag HTML se presenti e assolutamente non tradurre le chiavi 'testo', 'titolo' e 'pubblicazione':\n\n{testo}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def traduci_articolo_txt(file_path, cache):
    with open(file_path, encoding="utf-8") as f:
        contenuto = f.read()
    for lang in LANGUAGES:
        dest = file_path.parent / lang / f"{file_path.stem}_{lang}{file_path.suffix}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not is_updated(file_path, lang, cache) and dest.exists():
            continue
        print(f"✏️ Traduco {file_path.name} → {dest.name}")
        tradotto = traduci_testo(contenuto, lang)
        with open(dest, "w", encoding="utf-8") as out:
            out.write(tradotto)
        update_cache(file_path, lang, cache)

def traduci_json(file_path, cache):
    with open(file_path, encoding="utf-8") as f:
        dati = json.load(f)
    for lang in LANGUAGES:
        dest = file_path.with_stem(file_path.stem + f"_{lang}")
        if not is_updated(file_path, lang, cache) and dest.exists():
            continue
        print(f"✏️ Traduco {file_path.name} → {dest.name}")
        if isinstance(dati, list):
            tradotti = []
            for item in dati:
                item_copy = item.copy()
                for k in ["description", "descrizione", "Descrizione", "testo", "titolo"]:
                    if k in item:
                        item_copy[k] = traduci_testo(item[k], lang)
                tradotti.append(item_copy)
        else:
            tradotti = dati
        with open(dest, "w", encoding="utf-8") as out:
            json.dump(tradotti, out, ensure_ascii=False, indent=2)
        update_cache(file_path, lang, cache)

def main():
    cache = load_cache()
    for file in Path("articoli").glob("*.txt"):
        traduci_articolo_txt(file, cache)
    for file in Path("data").glob("prodotti.json") or file in Path("data").glob("pubblicita.json") or file in Path("data").glob("citazione.json"):
        traduci_json(file, cache)
    save_cache(cache)

if __name__ == "__main__":
    main()