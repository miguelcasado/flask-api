from app import app, db
from flask import render_template, flash, redirect, url_for
from forms import LoginForm, RegisterForm
from app.models import Usuario
from flask_login import login_user, current_user, logout_user,login_required

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('El correo ya está registrado.')
            return redirect(url_for('register'))

        new_user = Usuario(email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Te has registrado con éxito. Ahora puedes iniciar sesión.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Correo o contraseña incorrectos.')
            return redirect(url_for('login'))

        login_user(user)
        flash('Inicio de sesión exitoso.')
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/')
@login_required
def index():
    return render_template('index.html')  # or some other response

@app.route('/logout', methods=['POST'])
@login_required  # Protege esta ruta para que solo usuarios autenticados puedan acceder
def logout():
    logout_user()
    flash('Has cerrado sesión.')
    return redirect(url_for('login'))

