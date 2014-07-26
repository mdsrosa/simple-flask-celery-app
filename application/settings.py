__author__ = 'matheusrosa'

from application import app
import os

# configuracoes para a aplicacoa flasks
DATABASE = os.path.join(app.root_path, '../app.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# configuracoes para o celery
CELERY_DEFAULT_QUEUE = 'simple-flask-celery-app'
CELERY_DEFAULT_EXCHANGE = 'simple-flask-celery-app'
CELERY_DEFAULT_ROUTING_KEY = 'simple-flask-celery-app'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_TIMEZONE = 'America/Sao_Paulo'
CELERY_ENABLE_UTC = True
CELERY_BROKER_URL = 'amqp://guest@localhost//'