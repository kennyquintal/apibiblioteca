from app import app
from consultas.ObtenerCatalogos import obtenerCatalogos
from consultas.ObtenerLibros import obtenerLibros
from consultas.ObtenerBibliotecarios import obtenerBibliotecarios
from inserts.InsertarLibros import insertarLibro
from inserts.InsertarCliente import insertarClientes
from inserts.InsertarPrestamo import insertarPrestamo
from consultas.ObtenerClientes import obtenerClientes
from consultas.HistorialPrestamoLibro import historialPrestamoLibro
from consultas.ConsultarStatus import obtenerStatus
from consultas.ConsultarPrestamos import obtenerPrestamos
from consultas.HistorialPrestamoCliente import historialPrestamoCliente
from consultas.consultas_especificas.ConsultarLibro import obtenerLibro
from consultas.ObtenerDevoluciones import obtenerDevoluciones
from consultas.consultas_especificas.ObtenerDevolucionesPorCliente import obtenerDevolucionesPorCliente
from flask import flash,request,jsonify 
#from inserts.insertBibliotecario import insertarBibliotecario

@app.route('/api/devoluciones')
def devoluciones():
    devoluciones = obtenerDevoluciones()
    return jsonify(devoluciones)

@app.route('/api/devolucionesporcliente/<nombre_cliente>')
def devolucionesPorCliente(nombre_cliente):
    devoluciones_por_cliente = obtenerDevolucionesPorCliente(nombre_cliente)
    return jsonify(devoluciones_por_cliente)

@app.route('/api/clientes')
def clientes():
    clientes = obtenerClientes()
    return jsonify(clientes)

@app.route('/api/catalogos')
def catalogos():
    catalogo = obtenerCatalogos()
    return jsonify(catalogo)

@app.route('/api/libros')
def libros():
    libros = obtenerLibros()
    return jsonify(libros)

@app.route('/api/libro/<titulo_libro>')
def libroPortitulo(titulo_libro):
    libroPorTitulo = obtenerLibro(titulo_libro)
    return jsonify(libroPorTitulo)

@app.route('/api/status')
def consultarStatus():
    status = obtenerStatus()
    return jsonify(status)

@app.route('/api/prestamos')
def Prestamos():
    prestamos = obtenerPrestamos()
    return jsonify(prestamos)

@app.route('/api/historial_libro/<libro>')
def historialPrestamoLibros(libro):
    libros = historialPrestamoLibro(libro)
    return jsonify(libros)

@app.route('/api/historial_prestamo_cliente/<email>')
def historialPrestamoLibrosCliente(email):
    historial_prestamo_libros_cliente = historialPrestamoCliente(email)
    return jsonify(historial_prestamo_libros_cliente)

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

@app.route('/api/prestamo', methods = ['POST'])
def Prestamo():
    requestData = request.get_json()
    fechaPrestamo = requestData['fecha_de_prestamo']
    fechaDevolucion = requestData['fecha_devolucion']
    numeroEmpleado = requestData['fk_numempleado']
    idCliente = requestData['fk_cliente']
    idLibro = requestData['fk_libro']
    idStatus = requestData['fk_estatus']
    prestamo = insertarPrestamo(fechaPrestamo,fechaDevolucion,numeroEmpleado,idCliente,idLibro,idStatus)
    return prestamo

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