from nucleo.modelo.log_acciones_usuario import Log_acciones_usuario
from app_main.conexion import db
import datetime

def registrar_log(usuario,accion,tabla_objetivo,registro_objetivo):
    new_log = Log_acciones_usuario(
        usuario = usuario,
        accion = accion,
        tabla_objetivo = tabla_objetivo,
        registro_objetivo = registro_objetivo,
        fecha = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    )

    db.session.add(new_log)
    db.session.flush()
    if(new_log._id>0):
        db.session.commit()
        return True
    else:
        db.session.rollback()
        return False







    











