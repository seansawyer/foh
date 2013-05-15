"""Default settings common to all environments"""

import os

DEBUG = False

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
