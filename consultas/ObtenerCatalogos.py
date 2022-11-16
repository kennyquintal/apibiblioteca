from connection.coneccion import conn
from psycopg2.extras import RealDictCursor

def obtenerCatalogos():
    try:
        conexion = conn
        cursorCatalogo = conexion.cursor(cursor_factory=RealDictCursor)
        sql = "select * from catalogo;"
        ##conexion.commit()
        cursorCatalogo.execute(sql)
        conexion.commit()
        rows = cursorCatalogo.fetchall()
        #conexion.close()
        return rows
    except Exception as e:
        print(e)
    finally:
        #cursor.close()
        conexion.close()