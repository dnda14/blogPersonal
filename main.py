from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

articulos = [
    {"id": 0, "titulo": "Primer articulo", "contenido": "Este es el contenido del primer articulo"},
    {"id": 1, "titulo": "Segundo articulo", "contenido": "Este es el contenido del segundo articulo"},]


@app.get("/")
async def root():
    return {"message": "hola"}

@app.get("/articulos")
async def get_articulos():
    return {"data": articulos}


@app.get("/articulos/{id}")
async def get_articulos(id: int):
    articulos = get_articulos(id)
    return {"data": articulos[id]}

@app.post("/crear_articulo")
async def post_articulo(
    id:int,
    titulo: str,
    contenido: str
):
    return {"id":id, "titulo": titulo, "contenido": contenido}
    
    