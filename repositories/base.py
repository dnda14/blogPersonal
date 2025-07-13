import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def crear_tabla():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT NOT NULL
        ) 
                """)

    conn.commit()

