from nucleo.modelo.Ingrediente import Ingrediente
from app.conexion import db
from datetime import datetime

ahora = datetime.now()

def agregar(nombre, descripcion, cantidad_disponible,unidad_medida, usuario, fecha_registro):
    
    ingrediente = Ingrediente(
        nombre = nombre,
        descripcion = descripcion,
        cantidad_disponible = cantidad_disponible,
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
    ingredienteModificar.fecha_registro = fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
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

def consultar(_id):
    if _id == 0:
        return Ingrediente.query.all()
    else:
        return db.session.query(Ingrediente).filter(Ingrediente._id == _id).first()
