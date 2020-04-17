from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect, flash)
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__,
                 template_folder='templates')


@auth.route('/signup')
def signup():

    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_form():

    username = request.form.get('username')

    users = current_app.config['users']
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

    users = current_app.config['users']
    user = users.find_one({"username": username})
    print(user)

    if not user or not check_password_hash(user["password"], password):
        flash('The login details are incorrect')
        return redirect(url_for('auth.login'))

    return redirect(url_for('base.profile'))


@auth.route('/logout')
def logout():
    return 'Logout'
