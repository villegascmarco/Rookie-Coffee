import json 
from flask import Blueprint, jsonify, request,make_response
from nucleo.controlador import Controlador_Producto, Controlador_Ingrediente
from nucleo.controlador import controlador_inicio_sesion as sesion
#from nucleo.controlador import controlador_inicio_sesion as sesion
from app_main.conexion import db

producto_route = Blueprint('producto_route', __name__, url_prefix='/producto')


#Agrega un producto nuevo a la base de datos
@producto_route.route('/agregar', methods=['POST'])
@sesion.token_required('Usuario')
def agregarProducto(usuario_actual):
    try:
        if Controlador_Producto.agregar(
            request.json["nombre"],
            request.json["descripcion"],
            request.json["precio"],  
            request.json["fecha_registro"],
            request.json["ingrediente_producto"],
            usuario_actual._id):
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
@sesion.token_required('Usuario')
def modificarProducto(usuario_actual):
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
            request.json["ingrediente_producto"],
            usuario_actual._id):       
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
@sesion.token_required('Usuario')
def desactivarProducto(usuario_actual):  
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            }) 
        if Controlador_Producto.desactivar(request.json["_id"], usuario_actual._id):
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
@sesion.token_required('Usuario')
def reactivarProducto(usuario_actual):  
    try: 
        if "_id" not in request.json:
            return jsonify({
                "estado" : "ADVERTENCIA",
                "mensaje": "Ha ocurrido un error, es necesario proporcionar un id de usuario para desactivar"
            }) 
        if Controlador_Producto.reactivar(request.json["_id"], usuario_actual._id):
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
# @producto_route.route("/consultar", methods=['GET'])
# @sesion.token_required(['Usuario','Admin'])
# def consultarProductos(usuario_actual):
#     # try:
#     #consutamos todos los productos existentes
#     productos = Controlador_Producto.consultarallproducto()
#     producto_json = []
#     #setiamos los porductos
#     for producto in productos:
#         producto_dictionary = producto.__dict__
#         del producto_dictionary['_sa_instance_state']
        #consultamos la tabla de ingrediente producto
        # ingredientesP = Controlador_Ingrediente.consultarIngredientesXproducto(producto._id)
        # ingredientesP_json = []
        #setiamos los ingrediente producto
        # for ingredienteP in ingredientesP:
            # ingredientesP_dictionary = ingredienteP.__dict__
            #guardamos el id del ingrediente en una vaiable
            # idIngrediente = ingredienteP.ingrediente
            # eliminamos el nombre del valor 
            # del ingredientesP_dictionary["ingrediente"]
            #le cambiamos el nombre del valor junto con la variable
            # del ingredientesP_dictionary['_sa_instance_state']
            #consultamos los ingredientes en el producto con la id que guardamos en la variable 
            # ingredientesxproducto = Controlador_Ingrediente.consultarIngredientenProductos(idIngrediente)
            # ixp_json =[]
            # #setiamos la consulta para tener sus ingredientes 
            # for ingredientexproducto in ingredientesxproducto:
            #     # ixp_dictionary = ingredientexproducto.__dict__
            #     # del ixp_dictionary['_sa_instance_state']
            #     ixp_json.append(
            #         jsonify({
            #             "_id": ingredientexproducto._id,
            #             "cantidad_requerida":ingredienteP.cantidad_requerida,
            #             "ingrediente":ingredientexproducto.nombre
            #         })
            #     )
            #la agrgamos como arreglo en la lista de ingrediente producto    
            # ingredientesP_dictionary["ingredientes"]= ixp_json
            # ingredientesP_json.append(ingredientesP_dictionary)
        #     ingredientesP_json.append(
        #         jsonify({
        #             "_id":ingredienteP._id,
        #             "cantidad_requerida":ingredienteP.cantidad_requerida,
        #             "producto":ingredienteP.producto,
        #             "ingrediente":ingredienteP.ingrediente,
        #             "estatus":ingredienteP.estatus,
        #             "usuario":ingredienteP.usuario,
        #             "fecha_registro":ingredienteP.fecha_registro
        #         })
        #     )
        
        # producto_dictionary["ingrediente_producto"] = ingredientesP_json 
        # producto_json.append(producto_dictionary)
    # return make_response(jsonify(producto_json),200)
    # return make_response(jsonify(producto_json),200)
    # except Exception as e:
    #     estado = "ERROR"
    #     mensaje = "Ha ocurrido un error al modificar el registro! Por favor verificalo con un administrador o revisa tu solicitud"
        
    #     return jsonify({
    #         "estado"  : estado,
    #         "mensaje" : mensaje,
    #         "excepcion":str(e)
    #     })

@producto_route.route("/consultar", methods=['GET'])
@sesion.token_required(['Usuario','Admin'])
def consultarProductos(usuario_actual):
    #consutamos todos los productos existentes
    productos = Controlador_Producto.consultarallproducto()
    producto_json = []
    #setiamos los porductos
    for producto in productos:
        producto_dictionary = producto.__dict__
        del producto_dictionary['_sa_instance_state']
        #consultamos la tabla de ingrediente producto
        ingredientesP = Controlador_Ingrediente.consultarIngredientesXproducto(producto._id)
        ingredientesP_json = []
        #setiamos los ingrediente producto
        for ingredienteP in ingredientesP:
            ingredientesP_dictionary = ingredienteP.__dict__
            #guardamos el id del ingrediente en una vaiable
            idIngrediente = ingredientesP_dictionary["ingrediente"] 
            # eliminamos el nombre del valor 
            del ingredientesP_dictionary["ingrediente"]
            #le cambiamos el nombre del valor junto con la variable
            del ingredientesP_dictionary['_sa_instance_state']
            #consultamos los ingredientes en el producto con la id que guardamos en la variable 
            ingredientesxproducto = Controlador_Ingrediente.consultarIngredientenProductos(idIngrediente)
            ixp_json =[]
            #setiamos la consulta para tener sus ingredientes 
            for ingredientexproducto in ingredientesxproducto:
                ixp_dictionary = ingredientexproducto.__dict__
                del ixp_dictionary['_sa_instance_state']
                ixp_json.append(ixp_dictionary)
             #la agrgamos como arreglo en la lista de ingrediente producto    
        #    ingredientesP_dictionary["ingredientes"]= ixp_json
            ingredientesP_json.append(ingredientesP_dictionary)
        producto_dictionary["ingrediente_producto"] = ingredientesP_json 
        producto_json.append(producto_dictionary)
    return jsonify(producto_json)

### Buscar por la id el registro del producto 
@producto_route.route("/buscar", methods=['POST'])
@sesion.token_required('Usuario')
def buscarProductos(usuario_actual):
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