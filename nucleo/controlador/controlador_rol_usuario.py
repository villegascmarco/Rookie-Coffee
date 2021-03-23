from nucleo.modelo.rol_usuario import Rol_usuario
from app_main.conexion import db

def agregar(nombre,descripcion):
    rol_usuario = Rol_usuario(
        nombre = nombre,
        descripcion = descripcion,
    )

    db.session.add(rol_usuario)

    db.session.commit()

    return True

def modificar(_id,nombre,descripcion):
    rolModificar = db.session.query(Rol_usuario).filter(Rol_usuario._id == _id).first()
    rolModificar.nombre = nombre
    rolModificar.descripcion = descripcion

    db.session.add(rolModificar)

    db.session.commit()

    return True

def desactivar(_id):
    rolDesactivar = db.session.query(Rol_usuario).filter(Rol_usuario._id == _id).first()
    rolDesactivar.estatus = 'Inactivo'
    
    db.session.add(rolDesactivar)

    db.session.commit()

    return True


def reactivar(_id):
    rolReactivar = db.session.query(Rol_usuario).filter(Rol_usuario._id == _id).first()
    rolReactivar.estatus = 'Activo'
    
    db.session.add(rolReactivar)

    db.session.commit()

    return True

def consultar(_id):
    if _id == 0:
        return Rol_usuario.query.all()
    else:
        return db.session.query(Rol_usuario).filter(Rol_usuario._id == _id).first()


