from connection.coneccion import conn
from psycopg2.extras import RealDictCursor

def obtenerCatalogos():
    try:
        conexion = conn
        cursorCatalogo = conexion.cursor(cursor_factory=RealDictCursor)
        sql = "select * from catalogo;"
        ##conexion.commit()
        cursorCatalogo.execute(sql)
        rows = cursorCatalogo.fetchall()
        return rows
        #conexion.close()
    except Exception as e:
        print(e)
    finally:
        #cursor.close()
        conexion.close()