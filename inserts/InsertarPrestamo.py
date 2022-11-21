from connection.coneccion import host,database,user,password,port
import psycopg2

def insertarPrestamo(fecha_prestamo,fecha_devolucion,fk_numempleado,fk_cliente,fk_libro,fk_estatus):
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    cursorInsertarlibro = conn.cursor()
    query = f"""insert into prestamos (fecha_de_prestamo,fecha_devolucion,fk_numempleado,fk_cliente,fk_libro,fk_estatus)
    values ('{fecha_prestamo}', '{fecha_devolucion}', {fk_numempleado},{fk_cliente},{fk_libro},{fk_estatus})"""
    try:
        cursorInsertarlibro.execute(query)
        conn.commit()
        return "Se ingreso correctamente"
    except Exception as e:
        print(e)
        conn.rollback()
        return "no se ingresaron los datos"
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorInsertarlibro.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")
