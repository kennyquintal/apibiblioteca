from app import app
from consultas.ObtenerCatalogos import obtenerCatalogos
from consultas.ObtenerLibros import obtenerLibros
from inserts.InsertarLibros import insertarLibro
from connection.coneccion import conn
from flask import flash,request,jsonify 
from consultas.ObtenerBibliotecarios import obtenerBibliotecarios

@app.route('/api/catalogos')
def catalogos():
    catalogo = obtenerCatalogos()
    conn.close()
    return jsonify(catalogo)

@app.route('/api/libros')
def libros():
    libros = obtenerLibros()
    conn.close()
    return jsonify(libros)

@app.route('/api/libro/' , methods=['POST'])
def libro():
    requestData = request.get_json()
    autorLibro = requestData['Autor']
    edicionLibro = requestData['Edicion']
    editorialLibro = requestData['Editorial']
    fkCatalogo = requestData['fk_catalogo']
    tituloLibro = requestData['Titulo']
    #autor,edicion,editorial,fk_catalogo,titulo
    return insertarLibro(autorLibro,edicionLibro,editorialLibro,fkCatalogo,tituloLibro)

@app.route('/api/bibliotecario')
def bibliotecarios():
    return jsonify(obtenerBibliotecarios())


if __name__=="__main__":
    #app.run()
    app.run(debug=True)