#Importamos el objeto de la base de datos __init__.py
from app.conexion import db
from flask_sqlalchemy import SQLAlchemy

class Unidad_medida(db.Model):
    
    __tablename__ = 'Unidad_medida'
    _id = db.Column(db.String(4), primary_key=True)
    descripcion = db.Column(db.String(100))
    usuario = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.String(45))
    