import json
from flask import Blueprint
from flask import jsonify
from flask import request
from nucleo.controlador import controlador_usuario
from nucleo.controlador import controlador_inicio_sesion as sesion
from app_main.conexion import db

usuario_route = Blueprint("usuario_route", __name__,url_prefix='/usuario')

@usuario_route.route('/agregar', methods=['POST'])
@sesion.token_required('Admin')
def agregar(usuario_actual):
    try:
        if controlador_usuario.agregar(
            request.json["nombre"],
            request.json["apellido_1"],
            request.json["apellido_2"],
            request.json["rfc"],
            request.json["nombre_acceso"],
            request.json["contrasena"],
            request.json["rol_usuario"],
            usuario_actual._id):

            return jsonify({
                "estado" : "OK",
                "mensaje": "Usuario registrado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al agregar el registro! Por favor verificalo con un administrador o revisa tu solicitud"    
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })

    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al agregar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })


@usuario_route.route('/modificar',methods=['POST'])
@sesion.token_required('Admin')
def modificar(usuario_actual):
    try:    
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para modificar"
            })

        contrasena = ""

        if "contrasena" in request.json:
            contrasena = request.json["contrasena"]

        if controlador_usuario.modificar(
            request.json["_id"],
            request.json["nombre"],
            request.json["apellido_1"],
            request.json["apellido_2"],
            request.json["rfc"],
            request.json["nombre_acceso"],
            contrasena,
            request.json["rol_usuario"],
            usuario_actual._id
        ):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Usuario modificado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })


    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })

@usuario_route.route('/desactivar', methods=["POST"])
@sesion.token_required('Admin')
def desactivar(usuario_actual):
    try:    
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            })
        if controlador_usuario.desactivar(request.json["_id"],usuario_actual._id):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Usuario desactivado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al desactivar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })

@usuario_route.route('/reactivar', methods=["POST"])
@sesion.token_required('Admin')
def reactivar(usuario_actual):
    try:    
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            })
        if controlador_usuario.reactivar(request.json["_id"],usuario_actual._id):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Usuario reactivado correctamente"
            })
        else:
            estado = "ERROR"
            mensaje = "El usuario no puede ser reactivado (nombre de acceso duplicado)"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error al reactivar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion":str(e)
        })

@usuario_route.route('/consultar', methods=['POST'])
@sesion.token_required('Admin')
def consultar(usuario_actual):
    estado = "OK"
    mensaje = "Información consultada correctamente"

    try:
        print(request.json)
        print("_id" not in request.json)

        if "_id" not in request.json or request.json["_id"] == 0:
            print("test")
            usuarios = controlador_usuario.consultar(0)
            if len(usuarios)>0:
                usuarios_json = []
                for usuario in usuarios:
                    usuario_dictionary = usuario.__dict__
                    del usuario_dictionary['_sa_instance_state']
                    usuarios_json.append(usuario_dictionary)
                return jsonify(usuarios_json)            
        else:
            usuario = controlador_usuario.consultar(request.json["_id"])
            if usuario is None:
                return jsonify({
                    "estado" : "ADVERTENCIA",
                    "mensaje": "No se encontro un usuario con el id especificado"
                })
            usuario_dictionary = usuario.__dict__
            del usuario_dictionary['_sa_instance_state']

            return jsonify(usuario_dictionary)

            
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })