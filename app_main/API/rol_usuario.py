from flask import Blueprint
from flask import jsonify
from nucleo.modelo.rol_usuario import Rol_usuario
rol_usuario_route = Blueprint("rol_usuario_route", __name__,url_prefix='/rol-usuario')


@usuario_route.route('/agregar', methods=['POST','GET'])
def agregar():
    



    return "test"