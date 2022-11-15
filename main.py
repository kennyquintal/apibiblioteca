from app import app
from consultas.ObtenerCatalogos import obtenerCatalogos
from consultas.ObtenerLibros import obtenerLibros
from inserts.InsertarLibros import insertarLibro
from flask import flash,request,jsonify 

@app.route('/api/catalogos')
def catalogos():
    return jsonify(obtenerCatalogos())

@app.route('/api/libros')
def libros():
    return jsonify(obtenerLibros())

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

if __name__=="__main__":
    #app.run()
    app.run(debug=True)