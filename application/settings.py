__author__ = 'matheusrosa'

# configuracoes para a aplicacao flask
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# configuracao para o  sqlalchemy
SQLALCHEMY_DATABASE_URI = 'mysql://root:he0dgb3b@localhost/my_flask_app'

# configuracoes para o celery
CELERY_DEFAULT_QUEUE = 'simple-flask-celery-app'
CELERY_DEFAULT_EXCHANGE = 'simple-flask-celery-app'
CELERY_DEFAULT_ROUTING_KEY = 'simple-flask-celery-app'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_TIMEZONE = 'America/Sao_Paulo'
CELERY_ENABLE_UTC = True
CELERY_BROKER_URL = 'amqp://guest@localhost//'
