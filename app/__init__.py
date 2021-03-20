#Archivo de configuración que tiene la función de crear nuestra aplicación, iniciar la base de datos 
# y registrará nuestros modelos
#Importamos el módulo os
import os
#Importamos la clase Flask del módulo flask
from flask import Flask
#Importamos la clase LoginManager de flask_login
from flask_login import LoginManager
#Importamos la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

#Creamos una instancia de SQLAlchemy
db = SQLAlchemy()

#Método de inicio de la aplicación
def create_app():
    #Creamos una instancia de Flask
    app = Flask(__name__)
    #registro de blueprint
    from .API.producto_route import producto_route as producto_blueprint
    app.register_blueprint(producto_blueprint)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #Generamos la clave aleatoria de sesión Flask para crear una cookie con la inf. de la sesión
    app.config['SECRET_KEY'] = os.urandom(24)
    #Definimos la ruta a la BD: mysql://user:password@localhost/bd'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/rookie_coffee_db'

    db.init_app(app)
    @app.before_first_request
    def create_all():
        db.create_all()
        
    return app
    