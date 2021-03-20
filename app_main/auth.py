#Importamos los módulos a usar de flask
from flask import Blueprint, render_template, redirect, url_for, request, flash
#Importamos los módulos de seguridad para las funciones hash
from werkzeug.security import generate_password_hash, check_password_hash
#Importamos el méodo login_user, logout_user, login_required de flask_login
from flask_login import login_user, logout_user, login_required
#Importamos el modelo del usuario
from .models import User
#Importamos el objeto de la BD desde __init__
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    #Consultamos si existe un usuario ya registrado con el email.
    user = User.query.filter_by(email=email).first()

    #Verificamos si el usuario existe
    #Tomamos el password proporcionado por el usuario y lo hasheamos, 
    # y lo comparamos con el password de la base de datos.
    if not user or not check_password_hash(user.password, password):
        flash('El usuario y/o la contraseña son incorrectos')
        return redirect(url_for('auth.login')) #Si el usuario no existe o el password es incorrecto regresamos a login
    
    #Si llegamos a este punto sabemos que el usuario tiene datos correctos.
    #Creamos una sessión y logueamos al usuario
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    #Consultamos si existe un usuario ya registrado con el email.
    user = User.query.filter_by(email=email).first()

    if user: #Si se encontró un usuario, redireccionamos de regreso a la página de registro
        flash('El correo electrónico ya existe')
        return redirect(url_for('auth.signup'))

    #Creamos un nuevo usuario con los datos del formulario.
    # Hacemos un hash a la contraseña para que no se guarde la versión de texto sin formato
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    #Añadimos el nuevo usuario a la base de datos.
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    #Cerramos la sessión
    logout_user()
    return redirect(url_for('main.index'))