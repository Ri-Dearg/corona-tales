import os
from flask import Flask
from flask_pymongo import PyMongo


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    app.config['MONGO_DBNAME'] = 'corona_tales'
    app.config["MONGO_URI"] = os.getenv('MONGO_URI')

    app.config['taglist'] = set()
    app.config['stories'] = PyMongo(app).db.stories
    app.config['users'] = PyMongo(app).db.users

    from .base import base as base_blueprint
    app.register_blueprint(base_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    if __name__ == '__main__':
        app.run(host=os.environ.get('IP'),
                port=int(os.environ.get('PORT')),
                debug=True)

    return app
