from nucleo.modelo.venta import Venta
from nucleo.controlador.controlador_detalle_venta import crear as crear_detalle, buscar_producto, buscar_venta, eliminar_venta
from nucleo.controlador import controlador_usuario
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
        raise Exception("Formato JSON incorrecto.")

    requestJSON = request.json

    metodo_busqueda = obtener_validar(requestJSON, 'metodo_busqueda')
    print(metodo_busqueda)
    if metodo_busqueda == 'especifico':
        return consultar_especifico(requestJSON)
    if metodo_busqueda == 'dia':
        return consultar_dia(requestJSON)
    if metodo_busqueda == 'general':
        return consultar_general()
    if metodo_busqueda == 'semanal':
        return consultar_semanal(requestJSON)
    if metodo_busqueda == 'mensual':
        return consultar_mensual(requestJSON)

    raise Exception(
        f"{metodo_busqueda} no está dentro de las opciones válidas.")


def consultar_especifico(requestJSON):
    fecha_inicial = obtener_validar(requestJSON, 'fecha_inicial')
    validar_formato(fecha_inicial, 'fecha_inicial')

    fecha_final = obtener_validar(requestJSON, 'fecha_final')
    validar_formato(fecha_final, 'fecha_final')

    ventas = Venta.query.filter(
        Venta.fecha.between(fecha_inicial, fecha_final))

    ventas_json = []
    numero_registros = 0
    for venta in ventas:
        numero_registros += 1
        diccionario = venta.__dict__
        del diccionario['_sa_instance_state']
        diccionario['detalle_venta'] = buscar_venta(venta._id)
        diccionario['usuario'] = controlador_usuario.consultar(
            venta.usuario).nombre_acceso
        ventas_json.append(diccionario)
    return ventas_json, numero_registros

def consultar_dia(requestJSON):
    today = datetime.date.today()

    fecha_inicial = today.strftime('%Y-%m-%dT%H:%M:%S')
    fecha_final = str(today)+'T:23:59:59'

    ventas = Venta.query.filter(
        Venta.fecha.between(fecha_inicial, fecha_final))

    ventas_json = []
    numero_registros = 0
    for venta in ventas:
        numero_registros += 1
        diccionario = venta.__dict__
        del diccionario['_sa_instance_state']
        diccionario['detalle_venta'] = buscar_venta(venta._id)
        diccionario['usuario'] = controlador_usuario.consultar(
            venta.usuario).nombre_acceso
        ventas_json.append(diccionario)
    return ventas_json, numero_registros

def consultar_semanal(requestJSON):
    today = datetime.date.today()
    fecha_inicial = today - datetime.timedelta(days=today.weekday())
    fecha_final = fecha_inicial + datetime.timedelta(days=6)

    fecha_inicial = fecha_inicial.strftime('%Y-%m-%dT%H:%M:%S')
    fecha_final = str(fecha_final)+'T:23:59:59'

    ventas = Venta.query.filter(
        Venta.fecha.between(fecha_inicial, fecha_final))

    ventas_json = []
    numero_registros = 0
    for venta in ventas:
        numero_registros += 1
        diccionario = venta.__dict__
        del diccionario['_sa_instance_state']
        diccionario['detalle_venta'] = buscar_venta(venta._id)
        diccionario['usuario'] = controlador_usuario.consultar(
            venta.usuario).nombre_acceso
        ventas_json.append(diccionario)
    return ventas_json, numero_registros


def consultar_mensual(requestJSON):
    fecha_inicial = datetime.date.today().replace(day=1)
    fecha_final = fecha_inicial + datetime.timedelta(days=6)

    fecha_inicial = fecha_inicial.strftime('%Y-%m-%dT%H:%M:%S')
    print(fecha_inicial)
    fecha_final = str(last_day_of_month(fecha_final))+'T:23:59:59'
    print(fecha_final)

    ventas = Venta.query.filter(
        Venta.fecha.between(fecha_inicial, fecha_final))

    ventas_json = []
    numero_registros = 0
    for venta in ventas:
        numero_registros += 1
        diccionario = venta.__dict__
        del diccionario['_sa_instance_state']
        diccionario['detalle_venta'] = buscar_venta(venta._id)
        diccionario['usuario'] = controlador_usuario.consultar(
            venta.usuario).nombre_acceso
        ventas_json.append(diccionario)
    return ventas_json, numero_registros


def last_day_of_month(any_day):
    # this will never fail
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)


def consultar_general():
    ventas = Venta.query.all()

    ventas_json = []
    numero_registros = 0
    for venta in ventas:
        numero_registros += 1
        diccionario = venta.__dict__
        del diccionario['_sa_instance_state']
        diccionario['detalle_venta'] = buscar_venta(venta._id)
        diccionario['usuario'] = controlador_usuario.consultar(
            venta.usuario).nombre_acceso
        ventas_json.append(diccionario)
    return ventas_json, numero_registros


def buscar_id(_id):

    venta = Venta.query.filter(Venta._id == _id).first()

    diccionario = venta.__dict__
    del diccionario['_sa_instance_state']
    diccionario['detalle_venta'] = buscar_venta(venta._id)

    return diccionario


def validateFloat(value, atributo):
    try:
        raw_data = value[atributo]
        if type(raw_data) == int:
            raise Exception(f"Formato incorrecto en {atributo}")
        return float(raw_data)
    except Exception:
        raise Exception(f"Formato incorrecto en {atributo}")


def validateInt(value, atributo):
    try:
        raw_data = value[atributo]
        if type(raw_data) == float:
            raise Exception(f"Formato incorrecto en {atributo}")

        return int(raw_data)
    except Exception:
        raise Exception(f"Formato incorrecto en {atributo}")


def crear(request, usuario_actual):
    if not request.json:
        raise Exception(
            'JSON no encontrado. El JSON es necesario para procesar la petición.')

    requestJSON = request.get_json()

    fecha = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    total_venta = validateFloat(requestJSON, 'total_venta')
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
    try:
        db.session.commit()
    except Exception as e:
        if str(e).__contains__('IntegrityError'):
            raise Exception('El artículo no existe.')
        else:
            raise Exception(
                'Hubo un error interno. Por favor consultelo con un técnico.')
    return buscar_id(nueva_venta._id)


def modificar(request):
    if not request.json:
        raise Exception(
            'JSON no encontrado. El JSON es necesario para procesar la petición.')

    requestJSON = request.get_json()

    total_venta = validateFloat(requestJSON, 'total_venta')
    detalles = obtener_validar(requestJSON, 'detalles')
    _id = validateInt(requestJSON, '_id')

    venta_modificada = Venta.query.filter(
        Venta._id == _id).first()

    if not venta_modificada:
        raise Exception(
            'No hay ningún registro que coincida con el ID proporcionado.')

    venta_modificada.total_venta = total_venta

    db.session.add(venta_modificada)

    eliminar_venta(venta_modificada._id)
    crear_detalle(detalles, venta_modificada._id)
    try:
        db.session.commit()
    except Exception as e:
        if str(e).__contains__('IntegrityError'):
            raise Exception('El artículo no existe.')
        else:
            raise Exception(
                'Hubo un error interno. Por favor consultelo con un técnico.')
    return buscar_id(venta_modificada._id)


def desactivar(request):
    if not request.json:
        raise Exception(
            'JSON no encontrado. El JSON es necesario para procesar la petición.')

    requestJSON = request.json

    _id = validateInt(requestJSON, '_id')

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
