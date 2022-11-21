from connection.coneccion import host,database,user,password,port
import psycopg2

def insertarClientes(nombre,direccion,telefono,email):
    #conn = psycopg2.connect(host=host,database=database,user=user,password =password)
    conn = psycopg2.connect(host=host,database=database,user=user,password =password,port=port)
    cursorInsertarClientes = conn.cursor()
    query = f"""INSERT INTO cliente (nombre_cliente,direccion,telefono,email) 
    VALUES ('{nombre}','{direccion}','{telefono}','{email}');"""
    try:
        cursorInsertarClientes.execute(query)
        conn.commit()
        return "Se ingreso correctamente"
    except Exception as e:
        print(e)
        conn.rollback()
        return "no se ingresaron los datos"
    finally:
        print("Hay conexion?",conn.closed)
        if conn:
            cursorInsertarClientes.close()
            conn.close()
            print(conn.closed)
            print("conexion cerrada")