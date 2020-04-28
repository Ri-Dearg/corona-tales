import os

SECRET_KEY = os.getenv('SECRET_KEY')
MONGO_DBNAME = 'corona_tales'
MONGO_URI = os.getenv('MONGO_URI')

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
ADMINS = os.environ.get('ADMINS')
