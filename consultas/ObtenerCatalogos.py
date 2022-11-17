from connection.coneccion import host,database,user,password
from psycopg2.extras import RealDictCursor
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

#conexion = conn
def obtenerCatalogos():
    conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    sql = "select * from catalogo;"
    cursorCatalogo = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursorCatalogo.execute(sql)
        rows = cursorCatalogo.fetchall()
        conn.commit()
        return rows
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        conn.rollback()
        print("Se cerro la conexion en el except")
        #cursorCatalogo = conexion.cursor()
    finally:
        #conexion.close()
        if conn.closed != 0 :
            print(conn.closed)
            print("conexion abierta")
        else:
            print(conn.closed)
            print("conexion cerrada")