import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mi_clave_secreta_123'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

