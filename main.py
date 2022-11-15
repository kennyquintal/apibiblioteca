from app import app
from coneccion import conn
from flask import flash,request,jsonify 
#from psycopg2.extras import Json

@app.route('/api/catalogos')
def catalogos():
    try:
        conexion = conn
        cursorCatalogo = conexion.cursor()
        sql = "select * from catalogo;"
        ##conexion.commit()
        cursorCatalogo.execute(sql)
        rows = cursorCatalogo.fetchall()
        return jsonify(rows)
        #conexion.close()
    except Exception as e:
        print(e)
    finally:
        #cursor.close()
        conexion.close()
    


if __name__=="__main__":
    #app.run()
    app.run(debug=True)