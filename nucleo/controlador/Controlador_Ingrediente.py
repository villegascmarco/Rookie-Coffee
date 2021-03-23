from nucleo.modelo.Ingrediente import Ingrediente, Ingrediente_producto
from app.conexion import db
from datetime import datetime

ahora = datetime.now()

def agregar(nombre, descripcion, cantidad_disponible,unidad_medida, usuario, fecha_registro):
    
    if cantidad_disponible >=1000 and unidad_medida == "g":
        convercion = cantidad_disponible/1000
        unidad_medida = "kg"
    elif cantidad_disponible >=1000 and unidad_medida == "ml":
        convercion = cantidad_disponible/1000
        unidad_medida = "l"
    else: 
         convercion = cantidad_disponible   
         
    ingrediente = Ingrediente(
        nombre = nombre,
        descripcion = descripcion,
        cantidad_disponible = convercion,
        unidad_medida = unidad_medida,
        usuario = usuario,
        fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    )
    db.session.add(ingrediente)
    db.session.commit()
    return True


def modificar(_id, nombre, descripcion, cantidad_disponible,unidad_medida, usuario, fecha_registro):
    ingredienteModificar =  db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()
    ingredienteModificar.nombre = nombre
    ingredienteModificar.descripcion = descripcion
    ingredienteModificar.cantidad_disponible = cantidad_disponible
    ingredienteModificar.unidad_medida = unidad_medida
    ingredienteModificar.usuario = usuario
    fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    ingredienteModificar.fecha_registro = fecha_registro
    db.session.add(ingredienteModificar)
    db.session.commit()
    return True

def desactivar(_id):
    ingredienteDesactivar = db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()
    ingredienteDesactivar.estatus = 'Inactivo'
    db.session.add(ingredienteDesactivar)
    db.session.commit()
    return True

def reactivar(_id):
    ingredienteReactivar = db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()
    ingredienteReactivar.estatus = 'Activo'
    db.session.add(ingredienteReactivar)
    db.session.commit()
    return True

def consultarallIngredientes():
    return Ingrediente.query.all()

def consultar(_id):
    if _id == 0:
        return Ingrediente.query.all()
    else:
        return db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()


########### ACCIONES DE LA TABLA IGREDIENTE-PRODUCTO  ############################
def agregarIgrePro(nombre,cantidad_requerida ,producto ,ingrediente, usuario, fecha_registro):   
    ingredienteProducto = Ingrediente_producto(
        nombre = nombre,
        cantidad_requerida = cantidad_requerida,
        producto = producto,
        ingrediente = ingrediente,
        usuario = usuario,
        fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    )
    db.session.add(ingredienteProducto)
    db.session.commit()
    return True


def modificarIgrePro(_id, nombre, cantidad_requerida ,producto ,ingrediente, usuario, fecha_registro):
    ingredienteProductoModificar =  db.session.query().filter(Ingrediente_producto._id == _id).first()
    ingredienteProductoModificar.nombre = nombre
    ingredienteProductoModificar.cantidad_requerida = cantidad_requerida
    ingredienteProductoModificar.producto = producto
    ingredienteProductoModificar.ingrediente = ingrediente
    ingredienteProductoModificar.usuario = usuario
    fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    ingredienteProductoModificar.fecha_registro = fecha_registro
    db.session.add(ingredienteProductoModificar)
    db.session.commit()
    return True

def desactivarIgrePro(_id):
    ingredienteProductoDesactivar = db.session.query(Ingrediente_producto).filter(Ingrediente_producto._id == _id).first()
    ingredienteProductoDesactivar.estatus = 'Inactivo'
    db.session.add(ingredienteProductoDesactivar)
    db.session.commit()
    return True

def reactivarIgrePro(_id):
    ingredienteProductoReactivar = db.session.query(Ingrediente_producto).filter(Ingrediente_producto._id == _id).first()
    ingredienteProductoReactivar.estatus = 'Activo'
    db.session.add(ingredienteProductoReactivar)
    db.session.commit()
    return True

def consultarallIngredientesProductos():
    return Ingrediente_producto.query.all()

def consultarIngrePro(_id):
    if _id == 0:
        return Ingrediente_producto.query.all()
    else:
        return db.session.query(Ingrediente_producto).filter(Ingrediente_producto._id == _id).first()