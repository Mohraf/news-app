from distutils.command.config import config
from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

#Initialize the application
app = Flask(__name__, instance_relative_config=True)

# Set up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Initializing flask extensions
bootstrap = Bootstrap(app)

from app import views