
from pydantic import BaseModel
class Articulo(BaseModel):
    titulo : int
    contenido : str
    
    