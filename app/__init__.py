from distutils.command.config import config
from flask import Flask

#Initialize the application
app = Flask(__name__, instance_relative_config=True

# Set up configuration
# app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views