# DERPG #

## Local setup ##

Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html).

Install the [Heroku toolbelt](https://toolbelt.heroku.com/).
On Arch (using yaourt) just do this:

    yaourt heroku-toolbelt

If you are using rbenv and get a LoadError later, you may need to
install the Foreman gem explicitly.

    gem install foreman

Clone the repo.

    git clone git@github.com:seansawyer/derpg.git && cd derpg

Make yourself a virtualenv.

    mkvirtualenv --python=python2 derpg

Install dependencies.

    pip install -r requirements.txt

Start the app.

    foreman start

Visit the app at [http://localhost:5000/](http://localhost:5000/)

# Heroku setup #

Add the Heroku remote for deployment.

    heroku git:remote -a YOURAPP

# Deploy to Heroku #

Nothing special here.

    git push heroku master

Visit the app at [http://derp.herokuapp.com/](http://derp.herokuapp.com/)
