"""API routes"""

from derpg import app
from flask import jsonify

@app.route('/api/0.1/status')
def v0_1_status():
    return jsonify(ok=True)
