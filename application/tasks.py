__author__ = 'matheusrosa'
from application import app, celery, get_db
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@celery.task
def add_entry_task(title, text):
    with app.app_context():
        logger.info('Processing add_entry_task....')
        db = get_db()
        logger.info('I got the db object... %s' % db)
        db.execute('insert into entries (title, text) values (?, ?)',
               [title, text])
        logger.info('I inserted the informations: title: {0} text: {1}'.format(title, text))
        db.commit()
        logger.info('Now I commited to the database...')
        logger.info('Finished.')