from flask import (Blueprint, render_template, url_for, request,
                   redirect, flash)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .extensions import mongo
from .models import User

auth = Blueprint('auth', __name__,
                 template_folder='templates')

users = mongo.db.users


@auth.route('/signup')
def signup():

    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_form():

    username = request.form.get('username')
    user = users.find_one({"username": username})

    if user:
        flash('Username is taken')
        return redirect(url_for('auth.signup'))

    account = {'username': request.form.get('username'),
               'password': generate_password_hash(request.form.get
                                                  ('password'),
                                                  method='sha256')}
    users.insert_one(account)

    return redirect(url_for('base.story_page'))


@auth.route('/login')
def login():

    return render_template("login.html")


@auth.route('/login', methods=['POST'])
def login_form():

    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = users.find_one({"username": username})

    if not user or not check_password_hash(user["password"], password):
        flash('The login details are incorrect')
        return redirect(url_for('auth.login'))

    log_user = User(user.get('username'), password, _id=user.get('_id'))
    login_user(log_user, remember=remember)

    return redirect(url_for('base.profile'))


@auth.route('/logout')
def logout():
    return 'Logout'
