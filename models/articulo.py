
from pydantic import BaseModel
from typing import Optional

class Articulo(BaseModel):
    id: Optional[int] = None
    titulo : str
    contenido : str
    
class ResponseArticulo(BaseModel):
    message: str
    articulo: Articulo
    
class RequestArticulo(BaseModel):
    titulo: str
    contenido: str

class ArticuloUpdate(BaseModel):
    titulo: Optional[str] = None
    contenido: Optional[str] = None