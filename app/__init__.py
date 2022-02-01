from flask import Flask
from .config import DevConfig,ProdConfig
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__, instance_relative_config=True)

# Setting up configuration
app.config.from_object(ProdConfig)
app.config.from_pyfile('config.py')

# Initializing flask extensions
bootstrap = Bootstrap(app)

from app import views