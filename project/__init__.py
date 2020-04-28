import os
from flask import Flask
from flask_login import LoginManager
from .extensions import mongo, mail
from bson.objectid import ObjectId


def create_app():

    app = Flask(__name__)
    app.config.from_object('config')

    mongo.init_app(app)
    mail.init_app(app)

    app.config['taglist'] = set()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(ObjectId(user_id))

    from .base import base as base_blueprint
    app.register_blueprint(base_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    if __name__ == '__main__':
        app.run(host=os.environ.get('IP'),
                port=int(os.environ.get('PORT')),
                debug=True)

    return app
