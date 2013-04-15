"""Application setup"""

import os

from flask import Flask

app = Flask(__name__)

# load common settings for all environments
app.config.from_object('derpg.settings.default')

# load environment-specific settings, default to development
env = os.environ.get('FOH_ENV', 'development')
env_settings = 'derpg.settings.' + env
app.config.from_object(env_settings)

# import modules containing routes
from derpg import api, views
