from nucleo.modelo.usuario import Usuario
from app_main.conexion import db
from werkzeug.security import generate_password_hash

def agregar(nombre,apellido_1,apellido_2,rfc,nombre_acceso,contrasena,rol_usuario):
    hashed_password = generate_password_hash(contrasena, method='sha256')
    print(hashed_password)

    usuario = Usuario(
        nombre = nombre,
        apellido_1 = apellido_1,
        apellido_2 = apellido_2,
        rfc = rfc,
        nombre_acceso = nombre_acceso,
        contrasena = hashed_password,
        rol_usuario = rol_usuario
    )

    db.session.add(usuario)

    db.session.commit()
    return True
     
def modificar(_id,nombre,apellido_1,apellido_2,rfc,nombre_acceso,contrasena,rol_usuario):
    usuarioModificar = db.session.query(Usuario).filter(Usuario._id == _id).first()
    usuarioModificar.nombre = nombre
    usuarioModificar.apellido_1 = apellido_1
    usuarioModificar.apellido_2 = apellido_2
    usuarioModificar.rfc = rfc
    usuarioModificar.nombre_acceso = nombre_acceso
    hashed_password = generate_password_hash(contrasena, method='sha256')
    usuarioModificar.contrasena = hashed_password
    usuarioModificar.rol_usuario = rol_usuario
    
    db.session.add(usuarioModificar)
    
    db.session.commit()
    
    return True
    
def desactivar(_id):
    usuarioDesactivar = db.session.query(Usuario).filter(Usuario._id == _id).first()
    usuarioDesactivar.estatus = 'Inactivo'

    db.session.add(usuarioDesactivar)

    db.session.commit()

    return True

def reactivar(_id):
    usuarioReactivar = db.session.query(Usuario).filter(Usuario._id == _id).first()
    usuarioReactivar.estatus = 'Activo'

    db.session.add(usuarioReactivar)

    db.session.commit()

    return True

def consultar(_id):
    if _id == 0:
        return Usuario.query.all()
    else:
        return db.session.query(Usuario).filter(Usuario._id == _id).first()