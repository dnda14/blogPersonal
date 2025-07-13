
from pydantic import BaseModel
from typing import Optional

class Articulo(BaseModel):
    id: Optional[int] = None
    titulo : str
    contenido : str
    
    