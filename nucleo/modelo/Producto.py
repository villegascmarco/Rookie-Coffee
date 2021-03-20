#Importamos el objeto de la base de datos __init__.py
from usuario import Usuario
from flask_sqlalchemy import SQLAlchemy
#Importamos la clase UserMixin de  flask_login

class Producto(db.Model):
    
    __tablename__ = 'Producto'
    _id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
    precio = db.Column(db.Double)
    estatus = db.Column(db.String(64), nullable=False,default='Activo')
    usuario = db.relationship('Usuario')
    fecha_registro = db.Column(db.String(45))
    