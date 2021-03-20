from app.conexion import db
from flask_sqlalchemy import SQLAlchemy


class Rol_usuario(db.Model):
    __tablename__="rol_usuario"
    _id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(45), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    estatus = db.Column(db.String(64), nullable=False,default='Activo')
    


