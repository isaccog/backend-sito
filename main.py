
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/blog")
def get_blog():
    return [
        {"id": 1, "titolo": "Benvenuto", "testo": "Questo è il primo post del blog"},
        {"id": 2, "titolo": "Secondo Post", "testo": "Ecco un altro post interessante"},
    ]

@app.get("/immagini")
def get_immagini():
    return [
        {"id": 1, "url": "/static/img1.jpg", "didascalia": "Un bel tramonto"},
        {"id": 2, "url": "/static/img2.jpg", "didascalia": "Panorama montano"},
    ]
