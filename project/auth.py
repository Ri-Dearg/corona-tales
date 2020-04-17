from flask import (Blueprint, current_app, render_template, url_for, request,
                   redirect, flash)
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__,
                 template_folder='templates')

taglist = set()


@auth.route('/login')
def login():
    return 'Login'


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


@auth.route('/logout')
def logout():
    return 'Logout'
