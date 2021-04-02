from flask import Blueprint
from flask import jsonify, request
from nucleo.controlador import controlador_venta as controlador
from nucleo.controlador import controlador_inicio_sesion as sesion
venta_route = Blueprint("venta_route", __name__, url_prefix='/venta')


@venta_route.route('/test', methods=['POST', 'GET'])
def agregar():
    return "test"


@venta_route.route('/consultar', methods=['POST'])
@sesion.token_required
def consultar(usuario_actual):
    estado = ''
    mensaje = ''
    contenido = ''
    registros = 0

    try:

        ventas = controlador.buscar(request)

        estado = "OK"
        mensaje = "Información consultada correctamente"
        registros = ventas[1]
        contenido = ventas[0]

    except Exception as error:
        estado = "ERROR"
        mensaje = str(error)
        contenido = None
    return jsonify({"estado": estado, "mensaje": mensaje, "registros": registros, "contenido": contenido})


@venta_route.route('/consultar_general', methods=['POST'])
@sesion.token_required
def consultar_general(usuario_actual):
    estado = ''
    mensaje = ''
    contenido = ''
    registros = 0

    try:

        ventas = controlador.buscar_general(request)

        estado = "OK"
        mensaje = "Información consultada correctamente"
        registros = ventas[1]
        contenido = ventas[0]

    except Exception as error:
        estado = "ERROR"
        mensaje = str(error)
        contenido = None
    return jsonify({"estado": estado, "mensaje": mensaje, "registros": registros, "contenido": contenido})


@venta_route.route('/registrar', methods=['POST'])
@sesion.token_required
def registrar(usuario_actual):
    estado = ''
    mensaje = ''
    contenido = ''
    try:
        venta = controlador.crear(request, usuario_actual)

        estado = "OK"
        mensaje = "Venta registrada"
        contenido = venta

    except Exception as error:
        estado = "ERROR"
        mensaje = str(error)
        contenido = None

    return jsonify({"estado": estado, "mensaje": mensaje, "contenido": contenido})


@venta_route.route('/modificar', methods=['POST'])
@sesion.token_required
def modificar(usuario_actual):
    estado = ''
    mensaje = ''
    contenido = ''
    try:
        venta = controlador.modificar(request)

        estado = "OK"
        mensaje = "Venta registrada"
        contenido = venta

    except Exception as error:
        estado = "ERROR"
        mensaje = str(error)
        contenido = None

    return jsonify({"estado": estado, "mensaje": mensaje, "contenido": contenido})


@venta_route.route('/desactivar', methods=['POST'])
@sesion.token_required
def desactivar(usuario_actual):
    estado = ''
    mensaje = ''
    try:
        controlador.desactivar(request)

        estado = "OK"
        mensaje = "Venta eliminada"

    except Exception as error:
        estado = "ERROR"
        mensaje = str(error)

    return jsonify({"estado": estado, "mensaje": mensaje})
