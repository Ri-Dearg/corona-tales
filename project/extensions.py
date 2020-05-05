from flask_pymongo import PyMongo  # for working with mongodb
from flask_mail import Mail  # for sending email from the app

mongo = PyMongo()
mail = Mail()
