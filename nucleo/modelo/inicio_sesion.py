from app_main.conexion import db
from flask_sqlalchemy import SQLAlchemy

class Inicio_sesion(db.Model):
    __tablename__="inicio_sesion"
    _id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.Integer, nullable = False)
    fecha_inicio_sesion = db.Column(db.String(45), nullable=False)
    dispositivo = db.Column(db.String(50), nullable=False)
    direccion_ip = db.Column(db.String(20), nullable=False)
    estatus = db.Column(db.String(64), nullable=False,default='Activo')
    token = db.Column(db.String(300), nullable=False)
