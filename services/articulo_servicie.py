from ..repositories import database

con = database.Conexion()


def add_articulo_to_db(articulo_data: dict):
    con.add_articulo(articulo_data)
   

def get_articulos_from_db(int: id):
    datos = con.get_articulo_id(id)
    return datos

