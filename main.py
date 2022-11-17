from app import app
from consultas.ObtenerCatalogos import obtenerCatalogos
from consultas.ObtenerLibros import obtenerLibros
from consultas.ObtenerBibliotecarios import obtenerBibliotecarios
from inserts.InsertarLibros import insertarLibro
from inserts.InsertarCliente import insertarClientes
from flask import flash,request,jsonify 
#from inserts.insertBibliotecario import insertarBibliotecario


@app.route('/api/catalogos')
def catalogos():
    catalogo = obtenerCatalogos()
    return jsonify(catalogo)

@app.route('/api/libros')
def libros():
    libros = obtenerLibros()
    return jsonify(libros)

@app.route('/api/libro/' , methods=['POST'])
def libro():
    requestData = request.get_json()
    autorLibro = requestData['Autor']
    edicionLibro = requestData['Edicion']
    editorialLibro = requestData['Editorial']
    fkCatalogo = requestData['fk_catalogo']
    tituloLibro = requestData['Titulo']
    insertar_libros = insertarLibro(autorLibro,edicionLibro,editorialLibro,fkCatalogo,tituloLibro)
    return insertar_libros

@app.route('/api/cliente/', methods=['POST'])
def cliente():
    requestData = request.get_json()
    nombreCliente = requestData['Nombre']
    direccionCliente = requestData['Direccion']
    telefonoCliente = requestData['Telefono']
    emailCliente = requestData['Email']
    insertar_cliente = insertarClientes(nombreCliente,direccionCliente,telefonoCliente,emailCliente)
    return insertar_cliente

"""
@app.route('/api/bibliotecario', methods=['POST'])
def bibliotecarios():
    requestData = request.get_json()
    nombre = requestData['Nombre']
    email = requestData['Email']
    insertar = insertarBibliotecario(nombre, email)
    conectar.close()
    return insertar
"""
@app.route('/api/bibliotecarios')
def bibliotecario():
    bibliotecarios = obtenerBibliotecarios()
    return jsonify(bibliotecarios)

if __name__=="__main__":
    #app.run()
    app.run(debug=True)