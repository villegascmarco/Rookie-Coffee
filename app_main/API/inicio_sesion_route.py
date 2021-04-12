from flask import Blueprint
from flask import jsonify, request
from nucleo.controlador import controlador_inicio_sesion as sesion
from nucleo.controlador import controlador_rol_usuario
from nucleo.controlador import controlador_datos_entrada as datos
import datetime
from nucleo.modelo.usuario import Usuario
from flask import current_app
from werkzeug.security import check_password_hash
import jwt




inicio_sesion_route = Blueprint("inicio_sesion_route", __name__,url_prefix='/security')

@inicio_sesion_route.route('/login', methods=['POST'])  
# @datos.validar_solicitud
def login(): 
 
    auth = request.authorization   

    if not auth or not auth.username or not auth.password:  
        return jsonify({
                "estado":"ERROR",
                "mensaje":"Imposible autenticar, inicio de sesion no exitoso"
                })

    usuario = Usuario.query.filter_by(nombre_acceso=auth["username"],estatus='Activo').first()   

    if not usuario:
        return jsonify({
                "estado":"ERROR",
                "mensaje":"Usuario inexistente"
            })

    if sesion.consultar_por_usuario(usuario._id):
        if not sesion.logout(usuario._id):
            return jsonify({
                "estado":"ERROR",
                "mensaje":"Existe una sesion activa que impide continuar"
            })

    if usuario and check_password_hash(usuario.contrasena, auth["password"]):
        token = jwt.encode({'public_id': usuario._id, 'expiracion' : str(datetime.datetime.utcnow() + datetime.timedelta(minutes=30))}, current_app.config['SECRET_KEY'])  
        try:
            sesion.registrar_inicio_sesion(
                    usuario._id,
                    datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
                    request.json['dispositivo'],
                    request.json['direccion_ip'],
                    token.decode('UTF-8')
                )
        except Exception as e:
            return jsonify({
                    "estado":"ERROR",
                    "excepcion":str(e),
                    "mensaje":"Imposible autenticar, inicio de sesion no exitoso"
                })

        return jsonify({
                'token' : token.decode('UTF-8'),
                'rol': controlador_rol_usuario.consultar(usuario.rol_usuario).nombre,
                'nombre' : "{} {} {}".format(usuario.nombre,usuario.apellido_1,usuario.apellido_2),
                'nombre_acceso': usuario.nombre_acceso
            }) 

    return jsonify({
                    "estado":"ERROR",
                    "mensaje":"Imposible autenticar, inicio de sesion no exitoso"
            })

@inicio_sesion_route.route('/logout',methods=['POST'])
# @datos.validar_solicitud
@sesion.token_required("Any")
def logout(usuario_actual):
    try:
        if sesion.logout(usuario_actual._id):
            return jsonify({
                "estado" : "OK",
                "mensaje": "Se ha cerrado la sesion"
            })
        else:
            estado = "ERROR"
            mensaje = "Ha ocurrido un error al realizar la operacion!"
            return jsonify({
                "estado"  : estado,
                "mensaje" : mensaje
            })
    except Exception as e:
        return jsonify({
            "estado":"ERROR",
            "excepcion":str(e),
            "mensaje":"Imposible continuar"
        })

