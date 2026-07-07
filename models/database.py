from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100))
    precio = db.Column(db.Float)
    stock = db.Column(db.Integer)

    def __repr__(self):
        return f"<Producto {self.nombre}>"
    