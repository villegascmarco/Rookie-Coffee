from nucleo.modelo.usuario import Usuario
from nucleo.controlador import controlador_log_acciones_usuario as log
from nucleo.controlador import controlador_rol_usuario
from app_main.conexion import db
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

def agregar(nombre,apellido_1,apellido_2,rfc,nombre_acceso,contrasena,rol_usuario,usuario_actual_id):

    usuarioVerificar = db.session.query(Usuario).filter(Usuario.nombre_acceso == nombre_acceso).first()
    if not usuarioVerificar:
        usuario = Usuario(
            nombre = nombre,
            apellido_1 = apellido_1,
            apellido_2 = apellido_2,
            rfc = rfc,
            nombre_acceso = nombre_acceso,
            contrasena = generate_password_hash(contrasena, method='sha256'),
            rol_usuario = rol_usuario
        )

        db.session.add(usuario)
        
        db.session.flush()

        log.registrar_log(usuario_actual_id,'Agregar',Usuario.__tablename__,usuario._id)
        
        return True
    else:
        raise ValueError("El nombre de usuario proporcionado ya está registrado")
     
def modificar(_id,nombre,apellido_1,apellido_2,rfc,nombre_acceso,contrasena,rol_usuario,usuario_actual_id):
    usuarioModificar = db.session.query(Usuario).filter(Usuario._id == _id).first()
    usuarioModificar.nombre = nombre
    usuarioModificar.apellido_1 = apellido_1
    usuarioModificar.apellido_2 = apellido_2
    usuarioModificar.rfc = rfc
    usuarioModificar.nombre_acceso = nombre_acceso
    usuarioModificar.contrasena = generate_password_hash(contrasena, method='sha256')
    usuarioModificar.rol_usuario = rol_usuario
    
    db.session.add(usuarioModificar)
    
    log.registrar_log(usuario_actual_id,'Modificar',Usuario.__tablename__,_id)
    
    return True
    
def desactivar(_id,usuario_actual_id):
    usuarioDesactivar = db.session.query(Usuario).filter(Usuario._id == _id).first()
    usuarioDesactivar.estatus = 'Inactivo'

    db.session.add(usuarioDesactivar)

    log.registrar_log(usuario_actual_id,'Desactivar',Usuario.__tablename__,_id)

    return True

def reactivar(_id,usuario_actual_id):
    usuarioReactivar = db.session.query(Usuario).filter(Usuario._id == _id).first()
    usuarioReactivar.estatus = 'Activo'

    db.session.add(usuarioReactivar)

    log.registrar_log(usuario_actual_id,'Reactuvar',Usuario.__tablename__,_id)

    return True

def consultar(_id):
    if _id == 0:
        return Usuario.query.all()
    else:
        return db.session.query(Usuario).filter(Usuario._id == _id).first()

