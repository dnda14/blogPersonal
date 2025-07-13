import sqlite3
from contextlib import contextmanager



class Database:
    def __init__(self,db_name="database.db"):
        self.db_name = db_name
        self._initialize_db()

    @contextmanager
    def get_db(self):
        """Gestión segura de conexiones usando context manager"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()
            
    def _initialize_db(self):
        """Inicializa la base de datos si no existe"""
        with self.get_db() as conn:
            
            conn.cursor().execute("""
                CREATE TABLE IF NOT EXISTS articulos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    contenido TEXT NOT NULL
                )
            """)
            conn.commit()
    
    def get_all_articulos(self):    
        with self.get_db() as conn:
            cursor  = conn.cursor()
            cursor.execute("SELECT * FROM articulos")
            return cursor.fetchall()
        
            
    def get_articulo_by_id(self, id):
        with self.get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM articulos WHERE id = ?",(id,))
            return cursor.fetchone()
        

    def add_articulo(self, articulo_data: dict):
        with self.get_db() as conn:
            conn.cursor().execute(f"INSERT INTO articulos (titulo, contenido) VALUES ('{articulo_data['titulo']}', '{articulo_data['contenido']}')")
            conn.commit()




