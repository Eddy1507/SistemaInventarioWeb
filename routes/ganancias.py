from flask import Blueprint, render_template
from models.database import DetalleVenta

ganancias_bp = Blueprint("ganancias", __name__)


@ganancias_bp.route("/ganancias")
def ganancias():

    detalles = DetalleVenta.query.all()

    total_costo = 0
    total_venta = 0
    utilidad_total = 0

    productos = []

    for detalle in detalles:

        costo_total = detalle.costo_unitario * detalle.cantidad

        venta_total = detalle.precio * detalle.cantidad

        utilidad = venta_total - costo_total

        total_costo += costo_total

        total_venta += venta_total

        utilidad_total += utilidad

        productos.append({

            "codigo": detalle.producto.codigo,

            "nombre": detalle.producto.nombre,

            "costo": detalle.costo_unitario,

            "precio": detalle.precio,

            "cantidad": detalle.cantidad,

            "utilidad": utilidad

        })

    margen = 0

    if total_venta > 0:

        margen = (utilidad_total / total_venta) * 100

    labels = [p["nombre"] for p in productos]

    datos = [p["utilidad"] for p in productos]

    return render_template(

        "ganancias.html",

        productos=productos,

        total_costo=total_costo,

        total_venta=total_venta,

        utilidad_total=utilidad_total,

        margen=margen,

        labels=labels,

        datos=datos

    )
