from app import app, db

with app.app_context():
    db.create_all()  # Crea las tablas en la base de datos si no existen.

if __name__ == "__main__":
    app.run(debug=True)
