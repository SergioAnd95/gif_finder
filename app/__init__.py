from flask import Flask

from flask_pymongo import PyMongo

app = Flask(__name__)


app.config.from_object('app.settings')

mongo = PyMongo(app)

from .views import *
