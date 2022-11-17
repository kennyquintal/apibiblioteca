from connection.coneccion import host,database,user,password
from psycopg2.extras import RealDictCursor
import psycopg2
conn = psycopg2.connect(host,database,user,password)
def obtenerLibros():
    try:
        
        #conexion = conn
        cursorCatalogo = conn.cursor(cursor_factory=RealDictCursor)
        sql = "select * from libro;"
        cursorCatalogo.execute(sql)
        conn.commit()
        rows = cursorCatalogo.fetchall()
        #conn.close()
        return rows
    except Exception as e:
        print(e)
        #conn.rollback()
        return {"No hay libros"}
    finally:
        #conexion.close()
        if conn.closed == 0 :
            print(conn.closed)
            print("conexion abierta")
        else:
            print(conn.closed)
            print("conexion cerrada")