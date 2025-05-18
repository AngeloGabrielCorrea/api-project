from fastapi import FastAPI, Header, HTTPException
import json

app = FastAPI()
JSON_PATH = "anime_detalhes.json"
SECRET_KEY = "sua-chave-secreta-aqui"

@app.get("/")
def home():
    return {"msg": "API do AnimeFire - online"}

@app.get("/anime-detalhes.json")
def get_animes():
    with open(JSON_PATH, encoding='utf-8') as f:
        return json.load(f)

@app.post("/atualizar")
def atualizar_animes(x_api_key: str = Header(None)):
    if x_api_key != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Chave inválida")

    anime_lista = get_all_animes()
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(anime_lista, f, ensure_ascii=False, indent=2)
    return {"msg": "Atualizado com sucesso", "total": len(anime_lista)}
