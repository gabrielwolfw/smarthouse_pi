import json
import os
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import session, redirect, url_for, request, flash, render_template

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def create_user(username, password):
    users = load_users()
    if username in users:
        return False, "El usuario ya existe"
    users[username] = generate_password_hash(password)
    save_users(users)
    return True, "Usuario creado exitosamente"

def verify_user(username, password):
    users = load_users()
    if username not in users:
        return False
    return check_password_hash(users[username], password)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def setup_auth_routes(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            if verify_user(username, password):
                session['username'] = username
                return redirect(url_for('home'))
            flash('Usuario o contraseña incorrectos', 'error')
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            
            if password != confirm_password:
                flash('Las contraseñas no coinciden', 'error')
            else:
                success, message = create_user(username, password)
                flash(message, 'success' if success else 'error')
                if success:
                    return redirect(url_for('login'))
        return render_template('register.html')

    @app.route('/logout', methods=['POST'])
    def logout():
        session.pop('username', None)
        return redirect(url_for('login'))