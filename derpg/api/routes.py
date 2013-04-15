from derpg import app

@app.route('/')
def index():
    return 'Derp.'
