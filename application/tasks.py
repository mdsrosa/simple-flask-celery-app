__author__ = 'matheusrosa'
from application import app, celery, db
from application.models import Entry
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery.task
def add_entry_task(title, text):
    """
    Definicao da task para salvar um novo post
    :param title: titulo do post
    :param text: conteudo do post
    :return: None
    """
    with app.app_context():
        logger.info('Processing add_entry_task....')
        entry = Entry(title, text)
        db.session.add(entry)
        db.session.commit()
        logger.info('Finished.')
