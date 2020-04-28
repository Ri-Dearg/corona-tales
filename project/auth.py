from flask import (Blueprint, url_for, request,
                   redirect, flash)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .extensions import mongo
from .models import User

auth = Blueprint('auth', __name__,
                 template_folder='templates')

usersdb = mongo.db.users


@auth.route('/signup', methods=['POST'])
def signup_form():

    username = request.form.get('username')
    userID = username.upper()
    user = usersdb.find_one({"user_id": userID})

    if user:
        flash('Username is taken, please try another', 'sorry')
        return redirect(url_for('base.story_page'))

    account = {'username': username,
               'user_id': username.upper(),
               'password': generate_password_hash(request.form.get
                                                  ('password'),
                                                  method='sha256')}
    usersdb.insert_one(account)
    flash('Please Login, account created.', 'success')
    return redirect(url_for('base.story_page'))


@auth.route('/login', methods=['POST'])
def login_form():

    username = request.form.get('username')
    userID = request.form.get('username').upper()
    password = request.form.get('password')
    user = usersdb.find_one({"user_id": userID})

    remember = True if request.form.get('remember') else False

    if not user or not check_password_hash(user["password"], password):
        flash('The login details are incorrect', 'sorry')
        return redirect(url_for('base.story_page'))

    log_user = User(userID, username, password, _id=user.get('_id'))
    login_user(log_user, remember=remember)

    flash(f'Welcome, {username}', 'success')

    return redirect(url_for('base.profile'))


@auth.route('/change_password', methods=['POST'])
@login_required
def change_password():

    this_user = current_user.user_id
    user = usersdb.find_one({"user_id": this_user})
    password = request.form.get('password')

    if not check_password_hash(user["password"], password):
        flash('The password is incorrect', 'sorry')
        return redirect(url_for('base.profile'))

    usersdb.update({"user_id": this_user},
                   {'$set':
                    {'password': generate_password_hash(request.form.get
                                                        ('password-new'),
                                                        method='sha256')}
                    })

    flash('password has been changed', 'success')

    return redirect(url_for('base.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out', 'success')
    return redirect(url_for('base.story_page'))


@auth.route('/delete_stories', methods=['POST'])
@login_required
def delete_stories():

    password = request.form.get('password')
    this_user = current_user.user_id
    user = usersdb.find_one({"user_id": this_user})

    if not check_password_hash(user["password"], password):
        flash('The password is incorrect', 'sorry')
        return redirect(url_for('base.profile'))

    mongo.db.stories.remove({'user_id': this_user})
    flash('your stories have been deleted.', 'success')
    return redirect(url_for('base.profile'))


@auth.route('/delete_user', methods=['POST'])
@login_required
def delete_user():

    password = request.form.get('password')
    this_user = current_user.user_id
    user = usersdb.find_one({"user_id": this_user})

    if not check_password_hash(user["password"], password):
        flash('The password is incorrect', 'sorry')
        return redirect(url_for('base.profile'))

    mongo.db.stories.update_many({'user_id': this_user},
                                 {'$unset': {'user_id': ""}
                                  })
    usersdb.remove({'user_id': this_user})
    flash('account deleted', 'success')

    return redirect(url_for('base.story_page'))
