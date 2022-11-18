from connection.coneccion import host,database,user,password
from psycopg2.extras import RealDictCursor
import psycopg2

def obtenerPrestamos():
    conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    sql = f"""select pre.id_prestamos, c.nombre_cliente , l.titulo , b.nombre_empleado , e.estado, 
    pre.fecha_de_prestamo , pre.fecha_registro , pre.fecha_ultimaactualizacion
    from prestamos as pre 
    inner join cliente c on c.id_cliente = pre.fk_cliente 
    inner join libro l on l.id_libro  = pre.fk_libro 
    inner join bibliotecario b on b.no_empleado = pre.fk_numempleado
    inner join estatus e on e.id = pre.fk_estatus;"""
    cursorPrestamos = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursorPrestamos.execute(sql)
        rows = cursorPrestamos.fetchall()
        conn.commit()
        return rows
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        conn.rollback()
        return "No tiene datos"
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorPrestamos.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")