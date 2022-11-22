from connection.coneccion import host,database,user,password,port
from psycopg2.extras import RealDictCursor
import psycopg2
from consultas.ObtenerLibros import obtenerLibroTitulo 
from flask import jsonify 
import json

def historialPrestamoLibro(nombreLibro):
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    cursorPrestamoLibro = conn.cursor(cursor_factory=RealDictCursor)
    sql = f"""select titulo,nombre_cliente , fecha_de_prestamo , c.email,d.fecha_devolucion,r.fecha_de_renovacion , p.id_prestamos  
    from libro l
    LEFT JOIN  prestamos p  on l.id_libro  =p.fk_libro  
    LEFT JOIN cliente c on c.id_cliente = p.fk_cliente
    LEFT JOIN devolucion d on p.id_prestamos  = d.fk_prestamo
    LEFT JOIN renovacion r on p.id_prestamos  = r.fk_prestamo where l.titulo = '{nombreLibro}'"""
    try: 
        cursorPrestamoLibro.execute(sql)
        conn.commit()
        rows = cursorPrestamoLibro.fetchall()
        #accederemos al id de prestamos para saber si hay prestamos referente al libro buscado
        dato = jsonify(rows)
        datos = json.dumps(dato.get_json())
        data = json.loads(datos)
        prestamo = data[0]['id_prestamos']
        if obtenerLibroTitulo(nombreLibro):
            if rows:
                if prestamo is not None:
                    return rows
                else: return {"error":"No existe prestamos asociados a este libro"}
            else: return {"error": "No exite prestamos asociado a este libro"}
        else: return {"error": "no existe el libro"}
    except Exception as e:
        print("Error in transction Reverting all other operations of a transction ", e)
        return {"error":"Error algo salio mal"}
        conn.rollback()
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorPrestamoLibro.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")