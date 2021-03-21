from app_main.conexion import db
from flask_sqlalchemy import SQLAlchemy


class Detalle_venta(db.Model):

    __tablename__ = "detalle_venta"

    _id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_historico = db.Column(db.Float, nullable=False)
    estatus = db.Column(db.Integer, default=1, nullable=False)
    producto = db.Column(db.Integer, nullable=False)
    venta = db.Column(db.Integer, nullable=False)
