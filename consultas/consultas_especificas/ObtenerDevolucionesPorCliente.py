from connection.coneccion import host,database,user,password,port
from psycopg2.extras import RealDictCursor
import psycopg2

def obtenerDevolucionesPorCliente(nombre_cliente):
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    sql = f"""select d.id_devolucion, d.fecha_devolucion, c.nombre_cliente, l.titulo, 
    c2.categoria, e.estado, b.nombre_empleado
    from devolucion d
    left join prestamos p on p.id_prestamos = d.fk_prestamo
    left join cliente c on c.id_cliente = p.fk_cliente
    left join libro l on l.id_libro = p.fk_libro
    left join catalogo c2 on c2.id_catalogo = p.fk_estatus
    left join estatus e on e.id = fk_estatus
    left join bibliotecario b on b.no_empleado = p.fk_numempleado
    where c.nombre_cliente = '{nombre_cliente}';"""
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