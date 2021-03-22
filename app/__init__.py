from flask import Flask, jsonify
#Importamos la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from .conexion import DB_CONFIGURACION,db

from app.API.producto_route import producto_route 
from app.API.Unidad_medida_route import UnidadMedida_route
from app.API.ingrediente_route import ingrediente_route

#Método de inicio de la aplicación
def create_app():
    #Creamos una instancia de Flask
    app = Flask(__name__)

    app.register_blueprint(producto_route)
    app.register_blueprint(UnidadMedida_route)
    app.register_blueprint(ingrediente_route)

    app.config.from_json(DB_CONFIGURACION)

    db.init_app(app)
    @app.before_first_request
    def create_all():
        db.create_all()

    return app
    