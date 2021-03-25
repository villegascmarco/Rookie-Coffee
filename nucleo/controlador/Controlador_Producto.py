from nucleo.modelo.Producto import Producto
from nucleo.controlador import Controlador_Ingrediente
from app.conexion import db
from datetime import datetime

ahora = datetime.now()

def agregar(nombre, descripcion, precio, usuario, fecha_registro, objIngredienteProducto):
    
    producto = Producto(
        nombre = nombre,
        descripcion = descripcion,
        precio = precio,
        usuario = usuario,
        fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    )
    db.session.add(producto)
    db.session.flush() #ya tengo la ID
    for x in objIngredienteProducto:
       Controlador_Ingrediente.agregarIgrePro(x, usuario, producto._id)
    db.session.commit()
    return True, producto._id



def modificar(_id, nombre, descripcion, precio, usuario, fecha_registro):
    productoModificar =  db.session.query(Producto).filter(Producto._id == _id).first()
    productoModificar.nombre = nombre
    productoModificar.descripcion = descripcion
    productoModificar.precio = precio
    productoModificar.usuario = usuario
    fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    productoModificar.fecha_registro = fecha_registro
    db.session.add(productoModificar)
    db.session.commit()
    return True

def desactivar(_id):
    productoDesactivar = db.session.query(Producto).filter(Producto._id == _id).first()
    productoDesactivar.estatus = 'Inactivo'
    db.session.add(productoDesactivar)
    db.session.commit()
    return True

def reactivar(_id):
    productoReactivar = db.session.query(Producto).filter(Producto._id == _id).first()
    productoReactivar.estatus = 'Activo'
    db.session.add(productoReactivar)
    db.session.commit()
    return True

def consultar(_id):
    if _id == 0:
        return Producto.query.all()
    else:
        return db.session.query(Producto).filter(Producto._id == _id).first()
    
def consultarallproducto():
    return Producto.query.all()