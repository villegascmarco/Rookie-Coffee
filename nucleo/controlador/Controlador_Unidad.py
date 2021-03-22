from nucleo.modelo.Unidad_medida import Unidad_medida
from app.conexion import db
from datetime import datetime

ahora = datetime.now()

def agregar(_id,descripcion,usuario,fecha_registro):
    
    unidadMedida = Unidad_medida(
        _id = _id,
        descripcion = descripcion,
        usuario = usuario,
        fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    )
    db.session.add(usuario)
    db.session.commit()
    return True

def modificar(_id,descripcion,usuario,fecha_registro):
    productoModificar =  db.session.query(Unidad_medida).filter(Unidad_medida._id == _id).first()
    productoModificar._id = _id
    productoModificar.descripcion = descripcion
    productoModificar.usuario = usuario
    productoModificar.fecha_registro = fecha_registro = ahora.strftime("%d/%m/%Y  %H:%M:%S")
    db.session.add(productoModificar)
    db.session.commit()
    return True


def consultar():
    return Unidad_medida.query.all()
    