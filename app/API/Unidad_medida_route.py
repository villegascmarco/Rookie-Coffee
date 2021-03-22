import json 
from flask import Blueprint, jsonify, request
from nucleo.controlador import Controlador_Unidad
from app.conexion import db

UnidadMedida_route = Blueprint('UnidadMedida_route', __name__, url_prefix='/Unidad')


@UnidadMedida_route.route("/consultar", methods=['GET'])
def consultarUnidades():
    unidad = Controlador_Unidad.consultar()
    unidad_json = []
    for unidadmedida in unidad:
        unidad_dictionary = unidadmedida.__dict__
        del unidad_dictionary['_sa_instance_state']
        unidad_json.append(unidad_dictionary)
    return jsonify(unidad_json)
    
    