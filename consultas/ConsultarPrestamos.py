from connection.coneccion import host,database,user,password,port
from psycopg2.extras import RealDictCursor
import psycopg2

def obtenerPrestamos():
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    sql = f"""select p.id_prestamos, p.fecha_de_prestamo, p.fecha_devolucion , p.fecha_registro , p.fecha_ultimaactualizacion,c.nombre_cliente , l.titulo , b.nombre_empleado , e.estado
    from prestamos p 
    inner join libro l on l.id_libro  = p.fk_libro
    inner join cliente c on p.fk_cliente = c.id_cliente  
    inner join bibliotecario b on b.no_empleado = p.fk_numempleado
    inner join estatus e on e.id = p.fk_estatus
    where fk_libro = l.id_libro order by p.id_prestamos asc;"""
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