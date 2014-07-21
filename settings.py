__author__ = 'matheusrosa'

from app import app
import os

DATABASE = os.path.join(app.root_path, 'app.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'