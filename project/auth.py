from flask import (Blueprint, url_for, request,
                   redirect, flash)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .extensions import mongo
from .models import User

auth = Blueprint('auth', __name__,
                 template_folder='templates')

users = mongo.db.users


@auth.route('/signup', methods=['POST'])
def signup_form():

    username = request.form.get('username')
    userID = username.upper()
    user = users.find_one({"user_id": userID})

    if user:
        flash('Username is taken, please try another', 'sorry')
        return redirect(url_for('base.story_page'))

    account = {'username': username,
               'user_id': username.upper(),
               'password': generate_password_hash(request.form.get
                                                  ('password'),
                                                  method='sha256')}
    users.insert_one(account)
    flash('Account created successfully! Please Login.', 'success')
    return redirect(url_for('base.story_page'))


@auth.route('/login', methods=['POST'])
def login_form():

    username = request.form.get('username')
    userID = request.form.get('username').upper()
    password = request.form.get('password')
    user = users.find_one({"user_id": userID})

    remember = True if request.form.get('remember') else False

    if not user or not check_password_hash(user["password"], password):
        flash('The login details are incorrect', 'sorry')
        return redirect(url_for('base.story_page'))

    log_user = User(userID, username, password, _id=user.get('_id'))
    login_user(log_user, remember=remember)

    flash('Welcome, {{ username }}', 'success')

    return redirect(url_for('base.profile'))


@auth.route('/logout')
@login_required
def logout():
    flash('You have logged out', 'success')
    logout_user()
    return redirect(url_for('base.story_page'))


@auth.route('/delete_stories', methods=['POST'])
@login_required
def delete_stories():

    password = request.form.get('password')
    userID = current_user.user_id
    user = users.find_one({"user_id": userID})

    if not check_password_hash(user["password"], password):
        flash('The password is incorrect', 'sorry')
        return redirect(url_for('base.profile'))

    mongo.db.stories.remove({'user_id': userID})
    return redirect(url_for('base.profile'))
