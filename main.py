from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import json
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()  # carica da .env se esiste

URL_BASE = os.getenv("URL_BASE", "http://localhost:8000")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")

ARTICOLI_PATH = Path("articoli")

# Cartella dati
DATA_DIR = Path.cwd() / "data"

def read_json_file(name: str, lang: str = "it"):
    # Determina il nome file: prodotti_en.txt, prodotti_fr.txt, oppure prodotti.txt
    localized = f"{name}_{lang}.json" if lang != "it" else f"{name}.json"
    fallback = f"{name}.json"
    
    path = DATA_DIR / localized
    if not path.exists():
        path = DATA_DIR / fallback
        if not path.exists():
            return {"error": f"File {localized} o {fallback} non trovato"}
    
    text = path.read_text(encoding="utf-8").replace("{URL_BASE}", URL_BASE)
    return json.loads(text)

def parse_articolo_txt(path: Path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    articolo = {}
    testo_lines = []
    for line in lines:
        if line.startswith("id: "):
            articolo["id"] = line[4:].strip()
        elif line.startswith("titolo: "):
            articolo["titolo"] = line[8:].strip()
        elif line.startswith("pubblicazione: "):
            articolo["pubblicazione"] = line[15:].strip()
        elif line.startswith("testo:"):
            testo_lines = []
        else:
            testo_lines.append(line)

    testo = "<br>".join(testo_lines).replace("{URL_BASE}", URL_BASE)
    articolo["testo"] = testo
    return articolo

def carica_articoli(lang="it"):
    lang_path = ARTICOLI_PATH if lang == "it" else ARTICOLI_PATH / lang
    if not lang_path.exists():
        lang_path = ARTICOLI_PATH  # fallback

    return [parse_articolo_txt(p) for p in lang_path.glob("*.txt")]

@app.get("/blog")
def get_blog(request: Request):
    lang = request.query_params.get("lang", "it")
    return carica_articoli(lang)

@app.get("/blog/{post_id}")
def get_blog_post(post_id: str, request: Request):
    lang = request.query_params.get("lang", "it")
    posts = carica_articoli(lang)
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Articolo non trovato")

# Endpoint API
@app.get("/prodotti")
def get_prodotti(request: Request):
    lang = request.query_params.get("lang", "it")
    return read_json_file("prodotti", lang)

@app.get("/pubblicita")
def get_pubblicita(request: Request):
    lang = request.query_params.get("lang", "it")
    return read_json_file("pubblicita", lang)

@app.get("/citazioni")
def get_citazioni(request: Request):
    lang = request.query_params.get("lang", "it")
    return read_json_file("citazioni", lang)

