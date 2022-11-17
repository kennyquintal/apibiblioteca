from connection.coneccion import host,database,user,password
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

def insertarLibro(autor,edicion,editorial,fk_catalogo,titulo):
    conn = psycopg2.connect(host,database,user,password)
    try:
        ##fecha_registro
        #conexion = conn
        cursorInsertarlibro = conn.cursor()
        query = f"""INSERT INTO libro (autor,titulo,edicion,editorial,fk_catalogo) 
        VALUES ('{autor}','{titulo}','{edicion}','{editorial}',{fk_catalogo});"""
        cursorInsertarlibro.execute(query)
        conn.commit()
        #conexion.close()
        return "Se ingreso correctamente"
    except Exception as e:
        print(e)
        return "no se ingresaron los datos"
    finally:
        #conexion.close()
        if conn.closed == 0 :
            print(conn.closed)
            print("conexion abierta")
        else:
            print(conn.closed)
            print("conexion cerrada")
#me retorna la fecha y hora actual
def tiempoLocal():
    current_time = datetime.now()
    return current_time 
