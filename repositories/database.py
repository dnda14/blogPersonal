import sqlite3


class Conexion:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()


    def get_db():
        conn = sqlite3.conect("database.db")
        return conn

    def get_articulo_id(self, id):
        return self.cur.execute(f"SELECT * FROM articulos WHERE id = {id}").fetchone()

    def add_articulo(self, articulo_data):
        self.cur.execute(f"INSERT INTO articulos (titulo, contenido) VALUES ('{articulo_data['titulo']}', '{articulo_data['contenido']}')")



