from nucleo.modelo.detalle_venta import Detalle_venta
from app_main.conexion import db
import datetime
import json


def obtener_validar(json, atributo):

    valor = json.get(atributo)
    if not valor:
        raise Exception(f"Formato incorrecto en {atributo}")

    return valor


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
        detalles_json.append(diccionario)
    return detalles_json


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
        nuevo_detalle = Detalle_venta(
            cantidad=obtener_validar(detalle, 'cantidad'),
            precio_historico=obtener_validar(detalle, 'precio_historico'),
            producto=detalle.get('producto'),
            venta=venta)
        db.session.add(nuevo_detalle)

        # Restar al master del producto


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

        # Restar al master del producto


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
