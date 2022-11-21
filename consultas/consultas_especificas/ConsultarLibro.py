from connection.coneccion import host,database,user,password,port
from psycopg2.extras import RealDictCursor
import psycopg2

def obtenerLibro(titulo_libro):
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    sql = f"""select l.id_libro, l.autor, l.titulo, l.edicion, l.editorial, c.categoria, l.fecha_registro, l.fecha_ultimaactualizacion
    from libro l 
    left join catalogo c on c.id_catalogo = l.fk_catalogo
    where c.id_catalogo = l.fk_catalogo and l.titulo = '{titulo_libro}';"""
    cursorLibro = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursorLibro.execute(sql)
        rows = cursorLibro.fetchall()
        conn.commit()
        return rows
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        conn.rollback()
        return "No tiene datos"
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorLibro.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")