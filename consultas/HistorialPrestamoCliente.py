from connection.coneccion import host,database,user,password,port
from consultas.ObtenerClientes import obtenerClienteCorreo
from psycopg2.extras import RealDictCursor
import psycopg2

def historialPrestamoCliente(emailCliente):
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    cursorHistorialPrestamoLibro = conn.cursor(cursor_factory=RealDictCursor)
    sql = f"""
    select c.nombre_cliente ,titulo , fecha_de_prestamo , c.email ,d.fecha_devolucion,r.fecha_de_renovacion , p.id_prestamos  
    from libro l
    LEFT JOIN  prestamos p  on l.id_libro  =p.fk_libro  
    LEFT JOIN cliente c on c.id_cliente = p.fk_cliente
    LEFT JOIN devolucion d on p.id_prestamos  = d.fk_prestamo
    LEFT JOIN renovacion r on p.id_prestamos  = r.fk_prestamo where c.email  = '{emailCliente}';"""
    try: 
        cursorHistorialPrestamoLibro.execute(sql)
        conn.commit()
        rows = cursorHistorialPrestamoLibro.fetchall()
        if obtenerClienteCorreo(emailCliente):
            if rows:
                return rows
            else:
                return {"error": "No exite prestamos asociado a este cliente" }
        else: return {"error": "no existe el cliente"}
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        conn.rollback()
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorHistorialPrestamoLibro.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")