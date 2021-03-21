from flask import Blueprint
from flask import jsonify, request
import datetime
from nucleo.controlador import controlador_inicio_sesion
from nucleo.modelo.usuario import Usuario
from flask import current_app
from werkzeug.security import check_password_hash
import jwt


inicio_sesion_route = Blueprint("inicio_sesion_route", __name__,url_prefix='/security')

@inicio_sesion_route.route('/login', methods=['POST'])  
def login(): 
 
    auth = request.authorization   

    if not auth or not auth.username or not auth.password:  
        return jsonify({
                "estado":"ERROR",
                "mensaje":"Imposible autenticar, inicio de sesion no exitoso"
                })

    usuario = Usuario.query.filter_by(nombre_acceso=auth["username"]).first()   

    if usuario and check_password_hash(usuario.contrasena, auth["password"]):
        token = jwt.encode({'public_id': usuario._id, 'expiracion' : str(datetime.datetime.utcnow() + datetime.timedelta(minutes=30))}, current_app.config['SECRET_KEY'])  
        return jsonify({'token' : token.decode('UTF-8')}) 

    return jsonify({
                    "estado":"ERROR",
                    "mensaje":"Imposible autenticar, inicio de sesion no exitoso"
            })