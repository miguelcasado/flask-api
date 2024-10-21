# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

# Inicializa la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)  # Carga las configuraciones desde config.py

# Inicializa la base de datos y el manejo de sesiones
db = SQLAlchemy(app)

# Configuración de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Página de inicio de sesión
login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."

@login_manager.user_loader
def load_user(user_id):
    from app.models import Usuario  # Importar aquí para evitar el ciclo
    return Usuario.query.get(int(user_id))

# Importar rutas después de inicializar todo
from app import routes  # Solo importamos las rutas aquí
