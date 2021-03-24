from app_main.conexion import db
from flask_sqlalchemy import SQLAlchemy

class Log_acciones_usuario(db.Model):
    __tablename__="log_acciones_usuario"
    _id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(45), nullable = False)
    accion = db.Column(db.String(45), nullable = False)
    tabla_objetivo = db.Column(db.String(45), nullable = False)
    registro_objetivo = db.Column(db.Integer, nullable = False)
    fecha = db.Column(db.String(45), nullable = False)