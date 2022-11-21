from connection.coneccion import host,database,user,password,port
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

def insertarLibro(autor,edicion,editorial,fk_catalogo,titulo):
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    cursorInsertarlibro = conn.cursor()
    query = f"""INSERT INTO libro (autor,titulo,edicion,editorial,fk_catalogo) 
    VALUES ('{autor}','{titulo}','{edicion}','{editorial}',{fk_catalogo});"""
    try:
        cursorInsertarlibro.execute(query)
        conn.commit()
        return "Se ingreso correctamente"
    except Exception as e:
        print(e)
        conn.rollback()
        return "no se ingresaron los datos"
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorInsertarlibro.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")

#me retorna la fecha y hora actual
def tiempoLocal():
    current_time = datetime.now()
    return current_time 
