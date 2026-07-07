from flask import Blueprint, render_template
from models.database import Producto

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():

    total_productos = Producto.query.count()

    stock_bajo = Producto.query.filter(Producto.stock <= 5).count()

    inventario = Producto.query.all()

    valor_inventario = sum(
        producto.precio * producto.stock
        for producto in inventario
    )

    return render_template(
        "dashboard.html",
        total_productos=total_productos,
        stock_bajo=stock_bajo,
        valor_inventario=valor_inventario
    )