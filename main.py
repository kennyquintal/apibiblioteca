from app import app
from consultas.ObtenerCatalogos import obtenerCatalogos
from consultas.ObtenerLibros import obtenerLibros
from consultas.ObtenerBibliotecarios import obtenerBibliotecarios
from flask import flash,request,jsonify 

@app.route('/api/catalogos')
def catalogos():
    return jsonify(obtenerCatalogos())

@app.route('/api/libros')
def libros():
    return jsonify(obtenerLibros())

@app.route('/api/bibliotecario')
def bibliotecarios():
    return jsonify(obtenerBibliotecarios())

if __name__=="__main__":
    #app.run()
    app.run(debug=True)