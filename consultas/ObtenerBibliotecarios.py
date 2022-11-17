from connection.coneccion import host,database,user,password
from psycopg2.extras import RealDictCursor
import psycopg2

def obtenerBibliotecarios():
    conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    cursorCatalogo = conn.cursor(cursor_factory=RealDictCursor)
    sql = "select * from bibliotecario;"
    try: 
        cursorCatalogo.execute(sql)
        conn.commit()
        rows = cursorCatalogo.fetchall()
        return rows
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        conn.rollback()
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorCatalogo.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")