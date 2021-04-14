from nucleo.modelo.Producto import Producto
from nucleo.controlador import Controlador_Ingrediente
from app_main.conexion import db
from datetime import datetime

ahora = datetime.now()
## este metodo agrega los productos a la base de datos  tanto como en la tabla de ingrediente producto,
# se agrega la cantidad que va requerir en el ingrediente producto
def agregar(nombre, descripcion, precio, fecha_registro, objIngredienteProducto, usuario):
    
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



def modificar(_id, nombre, descripcion, precio, objIngredienteProducto, usuario):
    productoModificar =  db.session.query(Producto).filter(Producto._id == _id).first()
    productoModificar.nombre = nombre
    productoModificar.descripcion = descripcion
    productoModificar.precio = precio
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