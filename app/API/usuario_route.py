from flask import Blueprint

usuario_route = Blueprint("usuario_route", __name__,url_prefix='/usuario')

@usuario_route.route('/agregar', methods=['POST','GET'])
def agregar():
    return "test"