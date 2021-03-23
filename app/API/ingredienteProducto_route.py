import json 
from flask import Blueprint, jsonify, request
from nucleo.controlador import Controlador_Ingrediente
from app.conexion import db

ingredienteProducto_route = Blueprint('ingredienteProducto_route', __name__, url_prefix='/ingredienteProducto')

#Agrega un Ingrediente producto nuevo a la base de datos
@ingredienteProducto_route.route('/agregar', methods=['POST'])
def agregarIngredienteProducto():
    try:
        if Controlador_Ingrediente.agregarIgrePro(
            request.json["nombre"],
            request.json["cantidad_requerida"],
            request.json["producto"],
            request.json["ingrediente"],
            request.json["usuario"],  
            request.json["fecha_registro"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "IngredienteProducto registrado correctamente"
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

# modidica los Ingredientes Producto  que estan almacenados en la base de datos 
# con la ID del Ingredientes Producto
@ingredienteProducto_route.route('/modificar', methods=['POST'])
def modificarIngredienteProducto():
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para modificar"
            })
        if Controlador_Ingrediente.modificarIgrePro(
            request.json["_id"],
            request.json["nombre"],
            request.json["cantidad_requerida"],
            request.json["producto"],
            request.json["ingrediente"],
            request.json["usuario"],  
            request.json["fecha_registro"]):       
            return jsonify({
                "estado" : "OK",
                "mensaje": "Ingrediente Producto modificado correctamente"
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
        
#cambia del estatus de activo a incativo del Ingrediente Producto
@ingredienteProducto_route.route('/desactivar', methods=['POST'])
def desactivarIngredienteProducto():  
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            }) 
        if Controlador_Ingrediente.desactivarIgrePro(request.json["_id"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Ingrediente producto desactivado correctamente"
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
        
        
#cambia del estatus de activo a incativo del Ingrediente Producto
@ingredienteProducto_route.route('/reactivar', methods=['POST'])
def activarIngredienteProducto():  
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            }) 
        if Controlador_Ingrediente.reactivarIgrePro(request.json["_id"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Ingrediente producto activado correctamente"
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
        
# Consulta todos los ingredintes Productos que estan almacenados en la base de datos
@ingredienteProducto_route.route("/consultar", methods=['GET'])
def consultarIngredientesProductos():
    ingredientesP = Controlador_Ingrediente.consultarallIngredientesProductos()
    ingredientesP_json = []
    for ingredienteP in ingredientesP:
        ingredientesP_dictionary = ingredienteP.__dict__
        del ingredientesP_dictionary['_sa_instance_state']
        ingredientesP_json.append(ingredientesP_dictionary)
    return jsonify(ingredientesP_json)


@ingredienteProducto_route.route("/buscar", methods=['POST'])
def buscarIngredientesProductos():
    estado = "OK"
    mensaje = "Información consultada correctamente"
    
    try:
        print(request.json)
        print("_id" not in request.json)
        
        if "_id" not in request.json or request.json["_id"] == 0:
            print("test")
            ingredientesP = Controlador_Ingrediente.consultarIngrePro(0)
            if len(ingredientesP)>0:
                ingredintesP_json = []
                for ingredienteP in ingredientesP:
                    ingredienteP_dictionary = ingredienteP.__dict__
                    del ingredienteP_dictionary['_sa_instance_state']
                    ingredintesP_json.append(ingredienteP_dictionary)
                return jsonify(ingredintesP_json)
        else:
            ingredienteP = Controlador_Ingrediente.consultarIngrePro(request.json["_id"])
            if ingredienteP is None:
                    return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro un Ingrediente con el id especificado"
                    })
            ingredienteP_dictionary = ingredienteP.__dict__
            del ingredienteP_dictionary['_sa_instance_state']
            return jsonify(ingredienteP_dictionary)
        
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })