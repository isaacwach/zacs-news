from flask import flask
from .config import DevConfig
from flask_bootstrap import Bootstrap 

def create_app(config_name):
    app= Flask(__name__)