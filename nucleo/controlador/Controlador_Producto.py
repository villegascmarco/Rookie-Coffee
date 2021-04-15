from nucleo.modelo.Producto import Producto
from nucleo.controlador import Controlador_Ingrediente
from app_main.conexion import db
from datetime import datetime
import cloudinary
import cloudinary.uploader
import os.path

ahora = datetime.now()
## este metodo agrega los productos a la base de datos  tanto como en la tabla de ingrediente producto,
# se agrega la cantidad que va requerir en el ingrediente producto
def agregar(nombre, descripcion, precio,foto, fecha_registro, objIngredienteProducto, usuario):
    url_id = subir_foto(foto)
    producto = Producto(
        nombre = nombre,
        descripcion = descripcion,
        precio = precio,
        foto=url_id,
        usuario = usuario,
        fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    )
    db.session.add(producto)
    db.session.flush() #ya tengo la ID
    for x in objIngredienteProducto:
       Controlador_Ingrediente.agregarIgrePro(x, usuario, producto._id)
    db.session.commit()
    return True, producto._id



def modificar(_id, nombre, descripcion, precio,foto, objIngredienteProducto, usuario):
    productoModificar =  db.session.query(Producto).filter(Producto._id == _id).first()
    productoModificar.nombre = nombre
    productoModificar.descripcion = descripcion
    productoModificar.precio = precio

    eliminar_foto(productoModificar.foto)
    productoModificar.foto=subir_foto(foto)

    productoModificar.usuario = usuario
    productoModificar.fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    db.session.add(productoModificar)
    Controlador_Ingrediente.eliminarIngrePro(productoModificar._id)
    for xd in objIngredienteProducto:
        Controlador_Ingrediente.agregarIgrePro(xd, usuario, _id)
    db.session.commit()
    return True

def desactivar(_id, usuario):
    productoDesactivar = db.session.query(Producto).filter(Producto._id == _id).first()
    productoDesactivar.estatus = 'Inactivo'
    db.session.add(productoDesactivar)
    Controlador_Ingrediente.desactivarIgrePro(productoDesactivar._id)
    db.session.commit()
    return True

def reactivar(_id, usuario):
    productoReactivar = db.session.query(Producto).filter(Producto._id == _id).first()
    productoReactivar.estatus = 'Activo'
    db.session.add(productoReactivar)
    Controlador_Ingrediente.reactivarIgrePro(productoReactivar._id)
    db.session.commit()
    return True

def consultar(_id):
    if _id == 0:
        return Producto.query.all()
    else:
        return db.session.query(Producto).filter(Producto._id == _id).first()
    
def consultarallproducto():
    return Producto.query.all()

def subir_foto(archivo):
    if not archivo:
        return ''
    cloudinary.config(
        cloud_name="dg8xjgxd0",
        api_key="571627822527218",
        api_secret="A778wE2JSx45FRKIcbhw7o5q7z8",
        api_proxy= 'http://proxy.server:3128')

    respuesta = cloudinary.uploader.upload(archivo)
   
    if type(respuesta) != dict:
        raise Exception(f"Hubo un problema al subir la foto al servidor")

    return respuesta['public_id']

def eliminar_foto(public_id):
    if not public_id:
        return

    cloudinary.config(
        cloud_name="dg8xjgxd0",
        api_key="571627822527218",
        api_secret="A778wE2JSx45FRKIcbhw7o5q7z8",
        api_proxy= 'http://proxy.server:3128')

    respuesta = cloudinary.uploader.destroy(public_id)

    if type(respuesta) != dict:
        raise Exception(f"Hubo un problema al subir la foto al servidor")

    return respuesta