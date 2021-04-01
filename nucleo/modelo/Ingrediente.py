#Importamos el objeto de la base de datos __init__.py
from app_main.conexion import db
from flask_sqlalchemy import SQLAlchemy

class Ingrediente(db.Model):
    
    __tablename__ = 'Ingrediente'
    _id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(45))
    cantidad_disponible = db.Column(db.Float)
    estatus = db.Column(db.String(64), nullable=False,default='Activo')
    unidad_medida = db.Column(db.String(4))
    usuario = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.String(45))
    

class Ingrediente_producto(db.Model):
    
     __tablename__ = 'Ingrediente_producto'
     _id = db.Column(db.Integer, primary_key=True)
     cantidad_requerida = db.Column(db.Float)
     producto = db.Column(db.Integer, nullable=False)
     ingrediente = db.Column(db.Integer, nullable=False)
     estatus = db.Column(db.String(64), nullable=False,default='Activo')
     usuario = db.Column(db.Integer, nullable=False)
     fecha_registro = db.Column(db.String(45))
    