from functools import wraps
from flask import current_app,request,jsonify
from nucleo.modelo.usuario import Usuario
from nucleo.modelo.rol_usuario import Rol_usuario
from nucleo.modelo.inicio_sesion import Inicio_sesion

from app_main.conexion import db
import datetime
import jwt 


def token_required(rol_admitido):
   def inner_decorator(f):
      def wrapped(*args, **kwargs):
         token = None
         print(rol_admitido)
         if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

         if not token:
            return jsonify({
                     'estado' : 'ERROR',
                     'mensaje': 'Se requiere un token para continuar'
                  })

         try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            expiracion = datetime.datetime.strptime(data["expiracion"], '%Y-%m-%d %H:%M:%S.%f')
            ahora = datetime.datetime.utcnow()

            if ahora > expiracion:
               return jsonify({
                     'estado' : 'SESION CADUCADA',
                     'mensaje': 'El token enviado ha caducado'})   

            usuario_actual = db.session.query(Usuario).filter(Usuario._id == data['public_id']).first()
            rol = db.session.query(Rol_usuario).filter(Rol_usuario._id == usuario_actual.rol_usuario).first()            
            
            sesion_iniciada =db.session.query(Inicio_sesion).filter(Inicio_sesion.usuario ==  data['public_id'], Inicio_sesion.estatus == 'Activo').first()
            
            
            if rol.nombre != rol_admitido:
               raise Exception('Acceso denegado, permisos insuficientes')


            if not(sesion_iniciada.token == token and sesion_iniciada.estatus == 'Activo'):
               return jsonify({
                     'estado' : 'TOKEN INVALIDO',
                     'mensaje': 'La sesion se ha cerrado'})   

         except Exception as e:
            return jsonify({
                     'estado' : 'ERROR',
                     'excepcion': str(e),
                     'mensaje': 'El token enviado es invalido'})

         return f(usuario_actual, *args, **kwargs)
      return wrapped
   return inner_decorator


#DEFINICIÓN DE DECORADOR PARA VALIDACIÓN DE TOKEN
# def token_required(f):
#    @wraps(f)
#    def decorator(*args, **kwargs):

#       token = None

#       if 'x-access-tokens' in request.headers:
#          token = request.headers['x-access-tokens']

#       if not token:
#          return jsonify({
#                   'estado' : 'ERROR',
#                   'mensaje': 'Se requiere un token para continuar'
#                })

#       try:
#          data = jwt.decode(token, current_app.config['SECRET_KEY'])
#          expiracion = datetime.datetime.strptime(data["expiracion"], '%Y-%m-%d %H:%M:%S.%f')
#          ahora = datetime.datetime.utcnow()

#          if ahora > expiracion:
#             return jsonify({
#                   'estado' : 'SESION CADUCADA',
#                   'mensaje': 'El token enviado ha caducado'})   

#          usuario_actual = db.session.query(Usuario).filter(Usuario._id == data['public_id']).first()
#          sesion_iniciada =db.session.query(Inicio_sesion).filter(Inicio_sesion.usuario ==  data['public_id'], Inicio_sesion.estatus == 'Activo').first()

#          if not(sesion_iniciada.token == token and sesion_iniciada.estatus == 'Activo'):
#             return jsonify({
#                   'estado' : 'TOKEN INVALIDO',
#                   'mensaje': 'La sesion se ha cerrado'})   

#       except Exception as e:
#          return jsonify({
#                   'estado' : 'ERROR',
#                   'excepcion': str(e),
#                   'mensaje': 'El token enviado es invalido'})

#       return f(usuario_actual, *args, **kwargs)
#    return decorator

def registrar_inicio_sesion(usuario,fecha_inicio_sesion,dispositivo,direccion_ip,token):
   inicio_sesion_registro = Inicio_sesion(
      usuario = usuario,
      fecha_inicio_sesion = fecha_inicio_sesion,
      dispositivo = dispositivo,
      direccion_ip = direccion_ip,
      token = token
   )   

   db.session.add(inicio_sesion_registro)

   db.session.commit()

   return True

def logout(_id):
   sesion_activa = consultar_por_usuario(_id)
   sesion_activa.estatus = 'Inactivo'
   sesion_activa.token = ''

   db.session.add(sesion_activa)

   db.session.commit()

   return True

def consultar(_id):
    if _id == 0:
        return Inicio_sesion.query.all()
    else:
        return db.session.query(Inicio_sesion).filter(Inicio_sesion._id == _id).first()

def consultar_por_usuario(_id):
    if _id == 0:
        return None
    else:
        return db.session.query(Inicio_sesion).filter(Inicio_sesion.usuario == _id, Inicio_sesion.estatus == 'Activo').first()
