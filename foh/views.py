"""UI routes"""

from foh import app

@app.route('/')
def index():
    return 'Derp.'

@app.route('/bikes/<int:id>')
def bikes(id):
    return 'Bike {0}'.format(id)
