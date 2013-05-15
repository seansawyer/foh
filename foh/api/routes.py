"""REST API routes"""

from flask import jsonify
from foh import app

@app.route('/')
def index():
    return jsonify(message='Derp.')
