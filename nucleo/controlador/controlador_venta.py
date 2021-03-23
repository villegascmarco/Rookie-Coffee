from nucleo.modelo.venta import Venta
from nucleo.controlador.controlador_detalle_venta import crear as crear_detalle, buscar_producto, buscar_venta, eliminar_venta
from app_main.conexion import db
import datetime


def validar_formato(fecha, atributo):
    try:
        datetime.datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S')

    except ValueError:
        raise ValueError(f"Formato incorrecto en {atributo}")


def obtener_validar(json, atributo):
    try:
        return json[atributo]

    except Exception:
        raise Exception(f"Formato incorrecto en {atributo}")


def buscar(request):
    if not request.json:
        raise Exception(
            'JSON no encontrado. El JSON es necesario para procesar la petición.')

    requestJSON = request.json

    fecha_inicial = obtener_validar(requestJSON, 'fecha_inicial')
    validar_formato(fecha_inicial, 'fecha_inicial')

    fecha_final = obtener_validar(requestJSON, 'fecha_final')
    validar_formato(fecha_final, 'fecha_final')

    ventas = Venta.query.filter(
        (Venta.fecha.between(fecha_inicial, fecha_final)) & (Venta.estatus == 1))

    ventas_json = []
    numero_registros = 0
    for venta in ventas:
        numero_registros += 1
        diccionario = venta.__dict__
        del diccionario['_sa_instance_state']
        diccionario['detalle_venta'] = buscar_venta(venta._id)
        ventas_json.append(diccionario)
    return ventas_json, numero_registros


def buscar_id(_id):

    venta = Venta.query.filter(Venta._id == _id).first()

    diccionario = venta.__dict__
    del diccionario['_sa_instance_state']
    diccionario['detalle_venta'] = buscar_venta(venta._id)

    return diccionario


def crear(request, usuario_actual):
    if not request.json:
        raise Exception(
            'JSON no encontrado. El JSON es necesario para procesar la petición.')

    requestJSON = request.get_json()

    fecha = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    total_venta = obtener_validar(requestJSON, 'total_venta')
    usuario = usuario_actual._id
    detalles = obtener_validar(requestJSON, 'detalles')

    nueva_venta = Venta(
        fecha=fecha,
        total_venta=total_venta,
        estatus=1,
        usuario=usuario)

    db.session.add(nueva_venta)

    db.session.flush()  # Get inserted ID
    crear_detalle(detalles, nueva_venta._id)
    db.session.commit()
    return buscar_id(nueva_venta._id)


def modificar(request):
    if not request.json:
        raise Exception(
            'JSON no encontrado. El JSON es necesario para procesar la petición.')

    requestJSON = request.get_json()

    total_venta = obtener_validar(requestJSON, 'total_venta')
    detalles = obtener_validar(requestJSON, 'detalles')
    _id = obtener_validar(requestJSON, '_id')

    venta_modificada = Venta.query.filter(
        Venta._id == _id).first()

    venta_modificada.total_venta = total_venta

    db.session.add(venta_modificada)

    eliminar_venta(venta_modificada._id)
    crear_detalle(detalles, venta_modificada._id)
    db.session.commit()
    return buscar_id(venta_modificada._id)


def eliminar(request):
    if not request.json:
        raise Exception(
            'JSON no encontrado. El JSON es necesario para procesar la petición.')

    requestJSON = request.json

    _id = obtener_validar(requestJSON, '_id')

    fecha = obtener_validar(requestJSON, 'fecha')
    validar_formato(fecha, 'fecha')

    venta = Venta.query.filter(
        (Venta._id == _id) & (Venta.fecha == fecha)).first()

    if not venta:
        raise Exception(
            'No hay ningún registro que coincida con la fecha y ID proporcionados.')

    if venta.estatus == 'Inactivo':
        raise Exception(
            'El registro ya había sido eliminado.')

    venta.estatus = 2
    db.session.add(venta)

    eliminar_venta(_id)
    db.session.commit()
