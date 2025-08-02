from repositories import database

db = database.Database()


def add_articulo_to_db(articulo_data: dict):
    db.add_articulo(articulo_data)
   
def get_articulos_from_db(id: int):
    datos = db.get_articulo_by_id(id)
    datos2 = dict(datos)
    return datos2

def get_all_articulos_from_db():
    datos = db.get_all_articulos()
    datos2 = [dict(dato) for dato in datos]
    return datos2

def update_articulo_in_db(id: int, articulo_data: dict):
    db.update_articulo(id, articulo_data)