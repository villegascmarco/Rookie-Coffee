import json 
from flask import Blueprint, jsonify, request
from nucleo.controlador import Controlador_Producto, Controlador_Ingrediente
#from nucleo.controlador import controlador_inicio_sesion as sesion
from app.conexion import db

producto_route = Blueprint('producto_route', __name__, url_prefix='/producto')


#Agrega un producto nuevo a la base de datos
@producto_route.route('/agregar', methods=['POST'])
#@sesion.token_required
def agregarProducto():
    try:
        if Controlador_Producto.agregar(
            request.json["nombre"],
            request.json["descripcion"],
            request.json["precio"],
            request.json["usuario"],  
            request.json["fecha_registro"],
            request.json["ingrediente_producto"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Producto registrado correctamente"
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
        
# modidica los productos que estan almacenados en la base de datos 
# con la ID del producto
@producto_route.route('/modificar', methods=['POST'])
def modificarProducto():
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para modificar"
            })
        if Controlador_Producto.modificar(
            request.json["_id"],
            request.json["nombre"],
            request.json["descripcion"],
            request.json["precio"],
            request.json["usuario"],
            request.json["Ingrediente_producto"]):       
            return jsonify({
                "estado" : "OK",
                "mensaje": "Producto modificado correctamente"
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

#cambia del estatus de activo a incativo del producto
@producto_route.route('/desactivar', methods=['POST'])
def desactivarProducto():  
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            }) 
        if Controlador_Producto.desactivar(request.json["_id"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Producto desactivado correctamente"
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
        
# vuelave a cambiar el estatus del producto a activo
@producto_route.route('/reactivar', methods=['POST'])
def reactivarProducto():  
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            }) 
        if Controlador_Producto.reactivar(request.json["_id"]):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Producto Ractivado correctamente"
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
        
        
 # Consulta todos los productos que estan almacenados en la base de datos
@producto_route.route("/consultar", methods=['GET'])
def consultarProductos():
    productos = Controlador_Producto.consultarallproducto()
    producto_json = []
    for producto in productos:
        producto_dictionary = producto.__dict__
        del producto_dictionary['_sa_instance_state']
        producto_json.append(producto_dictionary)
    return jsonify(producto_json)
    

### Buscar por la id el registro del producto 
@producto_route.route("/buscar", methods=['POST'])
def buscarProductos():
    estado = "OK"
    mensaje = "Información consultada correctamente"
    
    try:
        print(request.json)
        print("_id" not in request.json)
        
        if "_id" not in request.json or request.json["_id"] == 0:
            print("test")
            productos = Controlador_Producto.consultar(0)
            if len(productos)>0:
                productos_json = []
                for producto in productos:
                    producto_dictionary = producto.__dict__
                    del producto_dictionary['_sa_instance_state']
                    productos_json.append(producto_dictionary)
                return jsonify(productos_json)
        else:
            producto = Controlador_Producto.consultar(request.json["_id"])
            if producto is None:
                    return jsonify({
                        "estado" : "ADVERTENCIA",
                        "mensaje": "No se encontro un Producto con el id especificado"
                    })
            producto_dictionary = producto.__dict__
            del producto_dictionary['_sa_instance_state']
            return jsonify(producto_dictionary)
    
    except Exception as e:
        estado = "ERROR"
        mensaje = "Ha ocurrido un error! Por favor verificalo con un administrador"
        return jsonify({
            "estado"  : estado,
            "mensaje" : mensaje,
            "excepcion": str(e)
        })