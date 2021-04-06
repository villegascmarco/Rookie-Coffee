import json 
from flask import Blueprint, jsonify, request
from nucleo.controlador import Controlador_Ingrediente
from nucleo.controlador import controlador_inicio_sesion as sesion
from app_main.conexion import db

ingrediente_route = Blueprint('ingrediente_route', __name__, url_prefix='/ingrediente')


#Agrega un Ingrediente nuevo a la base de datos
@ingrediente_route.route('/agregar', methods=['POST'])
@sesion.token_required('Usuario')
def agregarIngrediente(usuario_actual):
    try:
        if Controlador_Ingrediente.agregar(
            request.json["nombre"],
            request.json["descripcion"],
            request.json["cantidad_disponible"],
            request.json["unidad_medida"],  
            request.json["fecha_registro"],
            usuario_actual._id):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Ingrediente registrado correctamente"
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

# modidica los Ingredientes  que estan almacenados en la base de datos 
# con la ID del Ingrediente
@ingrediente_route.route('/modificar', methods=['POST'])
@sesion.token_required('Usuario')
def modificarIngredinete(usuario_actual):
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para modificar"
            })
        if Controlador_Ingrediente.modificar(
            request.json["_id"],
            request.json["nombre"],
            request.json["descripcion"],
            request.json["cantidad_disponible"],
            request.json["unidad_medida"],  
            request.json["fecha_registro"],
            usuario_actual._id):       
            return jsonify({
                "estado" : "OK",
                "mensaje": "Ingrediente modificado correctamente"
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
        
#cambia del estatus de activo a incativo del Ingrediente
@ingrediente_route.route('/desactivar', methods=['POST'])
@sesion.token_required('Usuario')
def desactivarIngrediente(usuario_actual):  
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            }) 
        if Controlador_Ingrediente.desactivar(request.json["_id"], usuario_actual._id):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Ingrediente desactivado correctamente"
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
        
# vuelave a cambiar el estatus del Ingrediente a activo
@ingrediente_route.route('/reactivar', methods=['POST'])
@sesion.token_required('Usuario')
def reactivarIngrediente(usuario_actual):  
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            }) 
        if Controlador_Ingrediente.reactivar(request.json["_id"], usuario_actual._id):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Ingrediente Reactivado correctamente"
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

# Consulta todos los ingredintes que estan almacenados en la base de datos
@ingrediente_route.route("/consultar", methods=['GET'])
@sesion.token_required('Usuario')
def consultarIngredientes(usuario_actual):
    ingredientes = Controlador_Ingrediente.consultarallIngredientes()
    ingredientes_json = []
    for ingrediente in ingredientes:
        ingredientes_dictionary = ingrediente.__dict__
        del ingredientes_dictionary['_sa_instance_state']
        ingredientes_json.append(ingredientes_dictionary)
    return jsonify(ingredientes_json)



@ingrediente_route.route("/buscar", methods=['POST'])
@sesion.token_required('Usuario')
def buscarIngredientes(usuario_actual):
    estado = "OK"
    mensaje = "Información consultada correctamente"
    
    try:
        print(request.json)
        print("_id" not in request.json)
        
        if "_id" not in request.json or request.json["_id"] == 0:
            print("test")
            ingredientes = Controlador_Ingrediente.consultar(0)
            if len(ingredientes)>0:
                ingredintes_json = []
                for ingrediente in ingredientes:
                    ingrediente_dictionary = ingrediente.__dict__
                    del ingrediente_dictionary['_sa_instance_state']
                    ingredintes_json.append(ingrediente_dictionary)
                return jsonify(ingredintes_json)
        else:
            ingrediente = Controlador_Ingrediente.consultar(request.json["_id"])
            if ingrediente is None:
                    return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro un Ingrediente con el id especificado"
                    })
            ingrediente_dictionary = ingrediente.__dict__
            del ingrediente_dictionary['_sa_instance_state']
            return jsonify(ingrediente_dictionary)
        
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })