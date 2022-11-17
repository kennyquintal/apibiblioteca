from connection.coneccion import host,database,user,password
from psycopg2.extras import RealDictCursor
import psycopg2

def historialPrestamoLibro(nombreLibro):
    conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    cursorPrestamoLibro = conn.cursor(cursor_factory=RealDictCursor)
    sql = f"""select nombre,titulo , fecha_de_prestamo , c.email,d.fecha_devolucion,r.fecha_de_renovacion , p.id_prestamos  
    from libro l
    LEFT JOIN  prestamos p  on l.id_libro  =p.fk_libro  
    LEFT JOIN cliente c on c.id_cliente = p.fk_cliente
    LEFT JOIN devolucion d on p.id_prestamos  = d.fk_prestamo
    LEFT JOIN renovacion r on p.id_prestamos  = r.fk_prestamo where l.titulo = '{nombreLibro}'"""
    try: 
        cursorPrestamoLibro.execute(sql)
        conn.commit()
        rows = cursorPrestamoLibro.fetchall()
        return rows
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        conn.rollback()
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorPrestamoLibro.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")