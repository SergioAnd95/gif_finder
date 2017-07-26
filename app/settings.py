import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))

DEBUG = False

CONFIRMATION_TOKEN = os.environ.get('CONFIRMATION_TOKEN')

TOKEN = os.environ.get('TOKEN')

SECRET_KEY = os.environ.get('SECRET_KEY')

MONGO_URI = os.environ.get('MONGO_URI')

try:
    from .local_settings import *
except:
    pass