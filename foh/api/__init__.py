"""API routes"""

from flask import jsonify
from foh import app

@app.route('/api/0.1/status')
def v0_1_status():
    return jsonify(ok=True)
