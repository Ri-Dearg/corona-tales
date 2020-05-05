import os

SECRET_KEY = os.getenv('SECRET_KEY')  # Key used in login functions

MONGO_DBNAME = 'corona_tales'  # database info
MONGO_URI = os.getenv('MONGO_URI')

MAIL_SERVER = 'smtp.gmail.com'  # settings used for flask-mail
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMINS = os.environ.get('ADMINS')
