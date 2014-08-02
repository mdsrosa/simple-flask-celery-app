__author__ = 'matheusrosa'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from celery import Celery

app = Flask(__name__)
app.config.from_object('application.settings')

# configuracao para o celery
celery = Celery()
celery.add_defaults(app.config)

db = SQLAlchemy(app)
db.init_app(app)

import application.views
