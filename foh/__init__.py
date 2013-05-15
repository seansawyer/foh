"""Application setup"""

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# load common settings for all environments
app.config.from_object('foh.settings.default')

# load environment-specific settings, default to development
env = os.environ.get('FOH_ENV', 'development')
env_settings = 'foh.settings.' + env
app.config.from_object(env_settings)

sa = SQLAlchemy(app)

# import modules containing routes
from foh import api, views
