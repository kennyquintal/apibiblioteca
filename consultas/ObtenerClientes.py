from connection.coneccion import host,database,user,password,port
from psycopg2.extras import RealDictCursor
import psycopg2

def obtenerClientes():
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    sql = "select * from cliente;"
    cursorClientes = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursorClientes.execute(sql)
        rows = cursorClientes.fetchall()
        conn.commit()
        return rows
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        conn.rollback()
        return "No tiene datos"
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorClientes.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")

def obtenerClienteCorreo(email):
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    sql = f"""select cliente.email from cliente where email = '{email}'"""
    cursorClientes = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursorClientes.execute(sql)
        rows = cursorClientes.fetchall()
        conn.commit()
        return rows
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        conn.rollback()
        return "No tiene datos"
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorClientes.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")

