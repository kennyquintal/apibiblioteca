from connection.coneccion import host,database,user,password
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime


def insertarBibliotecario(nombre, email):
    conn = psycopg2.connect(host,database,user,password)
    try:
        myDB = conn.cursor()
        fecha_registro = datetime.now()
        print(fecha_registro)
        query = f"""INSERT INTO bibliotecario (nombre, email, fecha_registro) 
        VALUES ('{nombre}', '{email}', '{fecha_registro}');"""
        myDB.execute(query)
        conn.commit()
        #myDB.close()
        return "Se ingresaron datos"
    except Exception as e:
        print(e)
        return "no se ingresaron los datos"
    finally:
        myDB.close()

