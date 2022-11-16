from connection.coneccion import conn
from psycopg2.extras import RealDictCursor
from datetime import datetime

def insertarLibro(autor,edicion,editorial,fk_catalogo,titulo):
    try:
        ##fecha_registro
        conexion = conn
        cursorInsertarlibro = conexion.cursor()
        query = f"""INSERT INTO libro (autor,titulo,edicion,editorial,fk_catalogo,fecha_registro) 
        VALUES ('{autor}','{titulo}','{edicion}','{editorial}',{fk_catalogo},'{tiempoLocal()}');"""
        cursorInsertarlibro.execute(query)
        conexion.commit()
        conexion.close()
        return "Se ingreso correctamente"
    except Exception as e:
        print(e)
        conn.close()
        return "no se ingresaron los datos"
    finally:
        conexion.close()
        cursorInsertarlibro.close()
        #cursorInsertarlibro.close()
#me retorna la fecha y hora actual
def tiempoLocal():
    current_time = datetime.now()
    return current_time 
