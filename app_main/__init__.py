
#Importamos la clase Flask del módulo flask
from flask import Flask, jsonify
#Importamos la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from .conexion import DB_CONFIGURACION,db

from .API.usuario_route import usuario_route
from .API.rol_usuario_route import rol_usuario_route
from .API.inicio_sesion_route import inicio_sesion_route

#Método de inicio de la aplicación
def create_app():
    #Creamos una instancia de Flask
    app = Flask(__name__)

    app.register_blueprint(usuario_route)
    app.register_blueprint(rol_usuario_route)
    app.register_blueprint(inicio_sesion_route)

    app.config.from_json(DB_CONFIGURACION)

    db.init_app(app)
    @app.before_first_request
    def create_all():
        db.create_all()

    return app
