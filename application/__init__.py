__author__ = 'matheusrosa'
import sqlite3

from flask import Flask, g
from celery import Celery

app = Flask(__name__)
app.config.from_object('application.settings')

# configuracao para o celery
celery = Celery()
celery.add_defaults(app.config)


def connect_db():
    """
    Connects to the database
    :return:
    """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('../schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    """
    Open a new database connection if there is none yet for the
    current application context.
    :return:
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """
    Close the database again at the end of the request.
    :return:
    """
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

import application.views