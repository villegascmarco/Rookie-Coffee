from app_main.conexion import db
from flask_sqlalchemy import SQLAlchemy
from .rol_usuario import Rol_usuario

class Usuario(db.Model):

    __tablename__ = "usuario"
    _id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido_1 = db.Column(db.String(45), nullable=False)
    apellido_2 = db.Column(db.String(45), nullable=False)
    rfc = db.Column(db.String(13), nullable=False)
    nombre_acceso = db.Column(db.String(45), nullable=False)
    contrasena = db.Column(db.String(64), nullable=False)
    estatus = db.Column(db.String(64), nullable=False,default='Activo')
    rol_usuario = db.Column(db.Integer, nullable = False)
    