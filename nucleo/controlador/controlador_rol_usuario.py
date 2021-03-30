from nucleo.modelo.rol_usuario import Rol_usuario
from nucleo.controlador import controlador_log_acciones_usuario as log
from app_main.conexion import db

def agregar(nombre,descripcion,usuario_actual_id):
    rol_usuario = Rol_usuario(
        nombre = nombre,
        descripcion = descripcion,
    )

    db.session.add(rol_usuario)

    db.session.flush()

    log.registrar_log(usuario_actual_id,'Agregar',Rol_usuario.__tablename__,rol_usuario._id)

    return True

def modificar(_id,nombre,descripcion,usuario_actual_id):
    rolModificar = db.session.query(Rol_usuario).filter(Rol_usuario._id == _id).first()
    rolModificar.nombre = nombre
    rolModificar.descripcion = descripcion

    db.session.add(rolModificar)

    log.registrar_log(usuario_actual_id,'Modificar',Rol_usuario.__tablename__,_id)

    return True

def desactivar(_id,usuario_actual_id):
    rolDesactivar = db.session.query(Rol_usuario).filter(Rol_usuario._id == _id).first()
    rolDesactivar.estatus = 'Inactivo'
    
    db.session.add(rolDesactivar)

    log.registrar_log(usuario_actual_id,'Desactivar',Rol_usuario.__tablename__,_id)

    return True


def reactivar(_id,usuario_actual_id):
    rolReactivar = db.session.query(Rol_usuario).filter(Rol_usuario._id == _id).first()
    rolReactivar.estatus = 'Activo'
    
    db.session.add(rolReactivar)

    log.registrar_log(usuario_actual_id,'Reactivar',Rol_usuario.__tablename__,_id)

    return True

def consultar(_id):
    if _id == 0:
        return Rol_usuario.query.all()
    else:
        return db.session.query(Rol_usuario).filter(Rol_usuario._id == _id).first()
