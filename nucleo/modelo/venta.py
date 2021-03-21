from app_main.conexion import db
from flask_sqlalchemy import SQLAlchemy


class Venta(db.Model):

    __tablename__ = "venta"
    __table_args__ = {'extend_existing': True}

    _id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(45), nullable=False)
    total_venta = db.Column(db.Float, nullable=False)
    estatus = db.Column(db.String(10), nullable=False)
    usuario = db.Column(db.Integer, nullable=False)
