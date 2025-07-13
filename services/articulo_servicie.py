from ..repositories import database

db = database.Database()


def add_articulo_to_db(articulo_data: dict):
    db.add_articulo(articulo_data)
   

def get_articulos_from_db(int: id):
    datos = db.get_articulo_by_id(id)
    return datos

