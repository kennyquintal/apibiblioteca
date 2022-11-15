from app import app
from consultas.ObtenerCatalogos import obtenerCatalogos
from flask import flash,request,jsonify 

@app.route('/api/catalogos')
def catalogos():
    return jsonify(obtenerCatalogos())

if __name__=="__main__":
    #app.run()
    app.run(debug=True)