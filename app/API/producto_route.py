from flask import Blueprint, jsonify
from nucleo.modelo.Producto import Producto
from flask_sqlalchemy import SQLAlchemy

producto_route = Blueprint('producto_route', __name__, url_prefix='/producto')


@producto_route.route("/prueba")
def prueba():
    products = Producto.query.all()
    for a in products:
        idpro = a._id
        nom = a.nombre
        desc = a.descripcion
        pre =  a.precio
        estatu = a.estatus
        usu = a.usuario
        fecha = a.fecha_registro
    return "xd"