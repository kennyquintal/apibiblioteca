from connection.coneccion import conn
from psycopg2.extras import RealDictCursor
from datetime import date


def insertarBibliotecario():
    myDB = conn.cursor()
    nombre = "Roger Quintal"
    email = "quintalkenny@gmail.com"
    fecha_registro = date.today()
    fecha_ultimaactualizacion = date.today()
    query = f"""INSERT INTO bibliotecario (nombre, email, fecha_registro, fecha_ultimaactualizacion VALUES ('{nombre}', '{email}', '{fecha_registro}', '{fecha_ultimaactualizacion}');"""
    myDB.execute(query)
    conn.commit()

    myDB.close()

