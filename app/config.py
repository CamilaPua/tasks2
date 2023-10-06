from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

# general config
FLASK_APP = 'app'
FLASK_DEBUG = True
SECRET_KEY = environ.get('SECRET_KEY')

# database
SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'
