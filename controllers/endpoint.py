from fastapi import APIRouter, HTTPException, status
from typing import List

from models.articulo import Articulo, ResponseArticulo, RequestArticulo, ArticuloUpdate


from services.articulo_service import (
    get_articulos_from_db, 
    get_all_articulos_from_db, 
    add_articulo_to_db
)


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
    
@router.put("/articulos/{id}", status_code=status.HTTP_200_OK)
async def update_articulo(
    id:int,
    datos: ArticuloUpdate
):
    articulo = get_articulos_from_db(id)
    if not articulo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Articulo not found"
        )
    articulo.titulo = datos.titulo if datos.titulo is not None else articulo.titulo
    articulo.contenido = datos.contenido if datos.contenido is not None else articulo.contenido
    