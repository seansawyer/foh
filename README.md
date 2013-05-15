# FOH #

Flask on Heroku - boilerplate for a simple Flask app.

## Prerequisites ##

The following items are prerequisites. Their installation is not
covered here:

* [Python 2.7](http://python.org/)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
* [PostgreSQL 9.x](http://www.postgresql.org/)

## Reading ##

If you're new to Python or Flask, you should read these things.

* [Official Python Tutorial](http://docs.python.org/2/tutorial/)
* [Learn Python the Hard Way](http://learnpythonthehardway.org/book/)
* [Flask Quickstart](http://flask.pocoo.org/docs/quickstart/)

If you're new to Heroku, read these things:

* [Heroku Platform Architecture](https://devcenter.heroku.com/categories/platform-architecture)
* [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/python)

## Differences from the Heroku Python starter app ##

There are a few differences/improvements here compared to Heroku's
[starter app](https://devcenter.heroku.com/articles/python):

* virtualenvwrapper instead of plain old `virtualenv
* IPython instead of the stock Python shell

## Local setup ##

Install the [Heroku toolbelt](https://toolbelt.heroku.com/).
On Arch (using yaourt) just do this:

    yaourt heroku-toolbelt

If you are using rbenv and get a LoadError later, you may need to
install the Foreman gem explicitly.

    gem install foreman

Clone the repo.

    git clone git@github.com:seansawyer/foh.git && cd foh

Make yourself a virtualenv.

    mkvirtualenv --python=python2 foh

Install dependencies.

    pip install -r requirements.txt

By default, the application assumes you are running in development and
loads settings from `foh/settings/default.py` and then from
`foh/settings/development.py`. This isn't magic; you can read the
code in `foh/__init__.py`.

If you want a custom enviroment, set the `FOH_ENV` enviroment
variable to the name of your environment and drop a new settings file
in `foh/settings`. So, say you added the following line to your
`.bashrc`:

    export FOH_ENV=sean

Then you would add `foh/settings/sean.py` and set things there.

## Database setup ##

If you like you may create a role to be used by the app from `psql`:

```
CREATE ROLE yourrolenamehere WITH LOGIN PASSWORD yourpasswordhere
```

Then edit the settings for your enviroment, filling in the user and
password:

```
SQLALCHEMY_DATABASE_URI = 'postgresql://USER:PASSWORD@localhost:5432/foh'
```

## Test things ##

Start the app:

    foreman start

Visit the app at [http://localhost:5000/](http://localhost:5000/)

# Heroku setup #

Create a new Heroku app if necessary.

    heroku apps:create YOURAPP

Otherwise, add the Git remote of a prexisting app for deployment.

    heroku git:remote -a YOURAPP

# Deploy to Heroku #

Nothing special here.

    git push heroku master

Visit the app at http://YOURAPP.herokuapp.com/
