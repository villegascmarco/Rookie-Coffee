from flask import Blueprint
from flask import jsonify
from nucleo.modelo.usuario import Usuario
usuario_route = Blueprint("usuario_route", __name__,url_prefix='/usuario')

@usuario_route.route('/agregar', methods=['POST','GET'])
def agregar():
    return "test"


@usuario_route.route('/consultar', methods=['POST','GET'])
def agregar():
    estado = "OK"
    mensaje = "Información consultada correctamente"

    try:
        usuarios  = Usuario.query.all()
        if len(usuarios)>0:
            for usuario in usuarios:
                print("jello")
        else:
            estado = "ADVERTENCIA"
            mensaje = "No hay registros para mostrar"
            return jsonify({
                "estado" : estado,
                "mensaje": mensaje
            })
    except:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje 
        })



    return "test"