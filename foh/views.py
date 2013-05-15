"""UI routes"""

from foh import app

@app.route('/')
def index():
    return 'Derp.'
