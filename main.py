from app import app
from consultas.ObtenerCatalogos import obtenerCatalogos
from consultas.ObtenerLibros import obtenerLibros
from flask import flash,request,jsonify 

@app.route('/api/catalogos')
def catalogos():
    return jsonify(obtenerCatalogos())

@app.route('/api/libros')
def libros():
    return jsonify(obtenerLibros())

if __name__=="__main__":
    #app.run()
    app.run(debug=True)