from flask import Blueprint, redirect, request, render_template
from werkzeug.security import generate_password_hash
from flask_security import login_user
import uuid

from database.classes import db, User, Role



register_page = Blueprint('register_page', __name__, template_folder='templates')
@register_page.route('/register', methods=['GET', 'POST'])
def registerpage():
    if request.method == 'GET':
        return render_template('auth/register.html')
    
    login = request.form.get('login')
    name = request.form.get('name')
    surname = request.form.get('surname')
    password = request.form.get('password')
    second_password = request.form.get('repeatPassword')

    role = db.session.query(Role).filter_by(name='user').first()
    user = db.session.query(User).filter_by(login=login).first()

    if not all([login, password, second_password, name, surname]) or password != second_password or len(password) < 6 or user:
        return redirect('/')
    
    fs_uniquifier = str(uuid.uuid4())
    
    new_user = User(login=login, name=name, surname=surname, password=generate_password_hash(password), active=True, fs_uniquifier=fs_uniquifier)
    new_user.roles.append(role)

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return redirect('/')