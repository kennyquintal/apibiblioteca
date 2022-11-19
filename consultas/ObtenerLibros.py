from connection.coneccion import host,database,user,password
from psycopg2.extras import RealDictCursor
import psycopg2

def obtenerLibros():
    conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    sql = "select * from libro;"
    try:
        cursorCatalogo = conn.cursor(cursor_factory=RealDictCursor)
        cursorCatalogo.execute(sql)
        rows = cursorCatalogo.fetchall()
        conn.commit()
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


def obtenerLibroTitulo(nombreLibro):
    conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    sql = f"""select l.titulo  from libro l where l.titulo = '{nombreLibro}'"""
    try:
        cursorCatalogo = conn.cursor(cursor_factory=RealDictCursor)
        cursorCatalogo.execute(sql)
        rows = cursorCatalogo.fetchall()
        conn.commit()
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
