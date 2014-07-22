__author__ = 'matheusrosa'
from application import app, celery, get_db


@celery.task
def add_entry_task(title, text):
    with app.app_context():
        print 'Processing add_entry_task....'
        db = get_db()
        print 'I got the db object...', db
        db.execute('insert into entries (title, text) values (?, ?)',
               [title, text])
        print 'Now I inserted the informations: title: %s and text: %s' % (title, text)
        db.commit()
        print 'Now I commited to the database...'
        print 'Finished.'