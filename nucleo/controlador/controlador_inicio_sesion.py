from functools import wraps
from flask import current_app,request,jsonify
from nucleo.modelo.usuario import Usuario
from app_main.conexion import db
import datetime
import jwt 

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):

      token = None

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
      except:
         return jsonify({
                  'estado' : 'ERROR',
                  'mensaje': 'El token enviado es invalido'})

      return f(usuario_actual, *args, **kwargs)
   return decorator