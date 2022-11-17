from app import app
#from consultas.ObtenerCatalogos import obtenerCatalogos
from consultas.ObtenerLibros import obtenerLibros
#from consultas.ObtenerBibliotecarios import obtenerBibliotecarios
#from inserts.InsertarLibros import insertarLibro
#from connection.coneccion import conectar
from flask import flash,request,jsonify 
#from inserts.insertBibliotecario import insertarBibliotecario


#@app.route('/api/catalogos')
#def catalogos():
#    catalogo = obtenerCatalogos()
#    return jsonify(catalogo)

@app.route('/api/libros')
def libros():
    libros = obtenerLibros()
    #conectar.closed
    return jsonify(libros)

"""@app.route('/api/libro/' , methods=['POST'])
def libro():
    #psycopg2.connect()
    print(conectar.closed)
    requestData = request.get_json()
    autorLibro = requestData['Autor']
    edicionLibro = requestData['Edicion']
    editorialLibro = requestData['Editorial']
    fkCatalogo = requestData['fk_catalogo']
    tituloLibro = requestData['Titulo']
    insertar_libros = insertarLibro(autorLibro,edicionLibro,editorialLibro,fkCatalogo,tituloLibro)
    conectar.close()
    return insertar_libros

@app.route('/api/bibliotecario', methods=['POST'])
def bibliotecarios():
    requestData = request.get_json()
    nombre = requestData['Nombre']
    email = requestData['Email']
    insertar = insertarBibliotecario(nombre, email)
    conectar.close()
    return insertar

@app.route('/api/bibliotecarios')
def bibliotecario():
    bibliotecarios = obtenerBibliotecarios()
    #conn.close()
    return jsonify(bibliotecarios)"""

if __name__=="__main__":
    #app.run()
    app.run(debug=True)