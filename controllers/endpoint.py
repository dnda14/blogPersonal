from fastapi import APIRouter, HTTPException, status
from typing import List

from models.articulo import Articulo


from services.articulo_servicie import (
    get_articulos_from_db, 
    get_all_articulos_from_db, 
    add_articulo_to_db
)
from datetime import datetime


router = APIRouter(prefix="/api/v1", tags=["articulos"])

@router.get("/articulos",response_model=List[Articulo])
async def get_articulos():
    try:
        return get_all_articulos_from_db()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/articulos/{id}")
async def get_articulo(id: int):
    articulos = get_articulos_from_db(id)
    return articulos

@router.post("/articulos",status_code=status.HTTP_201_CREATED) 
async def post_articulo(
    titulo: str,
    contenido: str
):
    return add_articulo_to_db({"titulo": titulo, "contenido": contenido})
    
    