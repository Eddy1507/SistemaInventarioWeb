from flask import Flask
from models.database import db
from flask import Flask, flash


from routes.dashboard import dashboard_bp
from routes.productos import productos_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "inventario2026"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(dashboard_bp)
app.register_blueprint(productos_bp)

if __name__ == "__main__":
    app.run(debug=True)