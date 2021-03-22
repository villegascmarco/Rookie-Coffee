import json 
from flask import Blueprint, jsonify, request
from nucleo.controlador import Controlador_Ingrediente
from app.conexion import db

ingrediente_route = Blueprint('ingrediente_route', __name__, url_prefix='/ingrediente')

@ingrediente_route.route("/consultar", methods=['POST','GET'])
def consultarIngredientes():
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
                        "mensaje": "No se encontro un usuario con el id especificado"
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