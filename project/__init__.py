# ---------------------------------------------------------------------
# A basic web app using flask for sharing stories through editable text
#
# (C) 2020 Rory Sheridan
# email sheridan.rp@gmail.com
# --------------------------------------------------------------------

import os
import re  # Regex function for the jinja filter
from flask import Flask
from flask_login import LoginManager
from .extensions import mongo, mail  # pymongo and flask-mail
from bson.objectid import ObjectId


def create_app():
    """Creates the app using configuration from config.py and blueprints."""
    app = Flask(__name__)
    app.config.from_object('config')  # The secret key, database and mail

    mongo.init_app(app)  # Starts pymongo
    mail.init_app(app)  # starts flask-mail

    app.config['taglist'] = set()  # Used for tag entry autocomplete

    login_manager = LoginManager()  # functions for flask-login
    login_manager.login_view = 'base.story_page'
    login_manager.init_app(app)

    from .models import User  # a model for users for flask-login

    @login_manager.user_loader
    def load_user(user_id):
        """Gets the correct user document for use by flask-login."""
        return User.get_by_id(ObjectId(user_id))

    def alpahanumeric_filter(s):
        """Creates a regex statement for use in a jinja filter"""
        symbols = re.compile('[^a-zA-Z\d]')
        return symbols.sub('', s)
    app.jinja_env.filters['alphanumeric'] = alpahanumeric_filter

    from .base import base as base_blueprint  # Basic site views
    app.register_blueprint(base_blueprint)

    # Views requiring entry of sensitive information
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    if __name__ == '__main__':
        app.run(host=os.environ.get('IP'),
                port=int(os.environ.get('PORT')))

    return app
