from nucleo.modelo.detalle_venta import Detalle_venta
from nucleo.controlador import Controlador_Ingrediente, Controlador_Producto
from app_main.conexion import db
import datetime
import json


def obtener_validar(json, atributo):

    valor = json.get(atributo)
    if not valor:
        raise Exception(f"Formato incorrecto en {atributo}")

    return valor


def validateInt(value, atributo):
    try:
        if type(value) == float:
            raise Exception(f"Formato incorrecto en {atributo}")

        return int(value)
    except Exception:
        raise Exception(f"Formato incorrecto en {atributo}")


def buscar_venta(venta):
    if not venta:
        raise Exception(
            'El atributo venta no debe estar vacío.')

    detalles_venta = db.session.query(Detalle_venta).filter(
        Detalle_venta.venta == venta, Detalle_venta.estatus == 1)

    detalles_json = []
    for detalle in detalles_venta:
        diccionario = detalle.__dict__
        del diccionario['_sa_instance_state']
        diccionario['producto'] = consultar_producto(diccionario['producto'])
        detalles_json.append(diccionario)
    return detalles_json


def consultar_producto(_id):
    producto = Controlador_Producto.consultar(_id)
    diccionario = producto.__dict__
    del diccionario['_sa_instance_state']
    return diccionario


def buscar_producto(producto):
    if not producto:
        raise Exception(
            'El atributo producto no debe estar vacío.')

    detalles_venta = db.session.query(Detalle_venta).filter(
        Detalle_venta.producto == producto).all

    return detalles_venta


def crear(detalles, venta):
    if type(detalles) != list:
        raise Exception(
            'Productos no válidos al validar el detalle.')

    for detalle in detalles:
        idProducto = validateInt(detalle.get('producto'), 'producto')
        nuevo_detalle = Detalle_venta(
            producto=idProducto,
            cantidad=validateInt(detalle.get('cantidad'),
                                 f'cantidad del producto {idProducto}'),
            precio_historico=validateInt(detalle.get(
                'precio_historico'), f'precio_historico del producto {idProducto}'),
            venta=venta)
        db.session.add(nuevo_detalle)

        # Restar al master del producto
        Controlador_Ingrediente.restarCantidadDisponible(
            idProducto, nuevo_detalle.cantidad)


def modificar(detalles, venta):
    if type(detalles) != list:
        raise Exception(
            'Productos no válidos al validar el detalle.')

    for detalle in detalles:
        antiguo_detalle = db.session.query(
            Detalle_venta).filter((Detalle_venta._id == detalle._id))

        nuevo_detalle = Detalle_venta(
            cantidad=obtener_validar(detalle, 'cantidad'),
            precio_historico=obtener_validar(detalle, 'precio_historico'),
            producto=detalle.get('producto'),
            venta=venta)
        db.session.add(nuevo_detalle)


def eliminar_venta(venta):
    if not venta:
        raise Exception(
            'El atributo venta no debe estar vacío.')

    detalles_venta = db.session.query(Detalle_venta).filter(
        Detalle_venta.venta == venta, Detalle_venta.estatus != 'Inactivo')

    for detalle in detalles_venta:

        if detalle.estatus == 'Inactivo':
            raise Exception(
                f"El detalle {detalle._id} relacionado a la venta {detalle.venta} ya había sido eliminado")

        detalle.estatus = 2
        detalle.cantidad *= -1
        db.session.add(detalle)
