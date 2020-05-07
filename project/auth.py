from flask import (Blueprint, url_for, request,
                   redirect, flash)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .extensions import mongo
from .models import User  # Class used as a blueprint for flask-login

auth = Blueprint('auth', __name__,
                 template_folder='templates')

usersdb = mongo.db.users


@auth.route('/signup', methods=['POST'])
def signup_form():
    """Creates a user document if the username isn't taken. Hashes password"""
    username = request.form.get('username')
    userID = username.upper()  # Creates a unique Id from the username
    user = usersdb.find_one({"user_id": userID})

    if user:  # Checks the unique ID to see if username is already taken
        flash('username is taken, please try another', 'sorry')
        return redirect(url_for('base.story_page'))

    # The scheme for the user document. The User class follows this scheme
    # so all fields are necessary.
    else:
        account = {'username': username,
                   'user_id': username.upper(),
                   'password': generate_password_hash(request.form.get
                                                      ('password'),
                                                      method='sha256'),
                   'prefill': {},
                   'liked': []}
        usersdb.insert_one(account)

        user = usersdb.find_one({"user_id": userID})
        flash('account created.', 'success')
        password = request.form.get('password')
        prefill = usersdb.find_one({"user_id": userID}, {'prefill'})
        liked = usersdb.find_one({"user_id": userID}, {'liked'})
        remember = False

        log_user = User(userID, username, password, prefill, liked,
                        _id=user.get('_id'))
        login_user(log_user, remember=remember)
        flash(f'Welcome, {username}', 'success')

        return redirect(url_for('base.profile'))


@auth.route('/login', methods=['POST'])
def login_form():
    """Logs user in securely after checking the details are correct. Will stay
    login if remember is checked."""
    username = request.form.get('username')
    userID = request.form.get('username').upper()
    password = request.form.get('password')
    user = usersdb.find_one({"user_id": userID})
    prefill = usersdb.find_one({"user_id": userID}, {'prefill'})
    liked = usersdb.find_one({"user_id": userID}, {'liked'})
    remember = True if request.form.get('remember') else False

    if not user or not check_password_hash(user["password"], password):
        flash('The login details are incorrect', 'sorry')
        return redirect(url_for('base.story_page'))

    # logs user in with flask-login, following the User model
    log_user = User(userID, username, password, prefill, liked,
                    _id=user.get('_id'))
    login_user(log_user, remember=remember)

    flash(f'Welcome, {username}', 'success')
    return redirect(url_for('base.profile'))


@auth.route('/change_password', methods=['POST'])
@login_required
def change_password():
    """Allows user to change their password after confirming details are
    correct"""

    this_user = current_user.user_id
    user = usersdb.find_one({"user_id": this_user})
    password = request.form.get('password')

    if not check_password_hash(user["password"], password):
        flash('The password is incorrect', 'sorry')
        return redirect(url_for('base.profile', _anchor='user-settings'))

    usersdb.update_one({"user_id": this_user},
                       {'$set':
                        {'password': generate_password_hash(request.form.get
                                                            ('password-new'),
                                                            method='sha256')}})

    flash('password has been changed', 'success')

    return redirect(url_for('base.profile', _anchor='user-settings'))


@auth.route('/delete_stories', methods=['POST'])
@login_required
def delete_stories():
    """Removes all stories with the user's ID attached from the database"""

    password = request.form.get('password')
    this_user = current_user.user_id
    user = usersdb.find_one({"user_id": this_user})

    # Checks if password is correct
    if not check_password_hash(user["password"], password):
        flash('The password is incorrect', 'sorry')
        return redirect(url_for('base.profile', _anchor='user-settings'))

    mongo.db.stories.remove({'user_id': this_user})
    flash('your stories have been deleted.', 'success')
    return redirect(url_for('base.profile', _anchor='user-settings'))


@auth.route('/delete_user', methods=['POST'])
@login_required
def delete_user():
    """Deletes the user from the database, but not their stories. Their ID is
    removed from the stories so it will not end up associated with any account
    with the same name."""
    password = request.form.get('password')
    this_user = current_user.user_id
    user = usersdb.find_one({"user_id": this_user})

    if not check_password_hash(user["password"], password):
        flash('The password is incorrect', 'sorry')
        return redirect(url_for('base.profile', _anchor='user-settings'))

    mongo.db.stories.update_many({'user_id': this_user},
                                 {'$unset': {'user_id': ""}})
    usersdb.remove({'user_id': this_user})
    flash('account deleted', 'success')

    return redirect(url_for('base.story_page'))


@auth.route('/logout')
@login_required
def logout():
    """Logs out user"""
    logout_user()
    flash('You have logged out', 'success')
    return redirect(url_for('base.story_page'))
