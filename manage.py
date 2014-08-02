# -*- coding: utf-8 -*-
__author__ = 'matheusrosa'

from application import app, db
from flask.ext.script import Manager

manager = Manager(app)


@manager.command
def init_db():
    """
    Criacao das tabelas
    """
    from application import models
    db.create_all()


@manager.command
def drop_db():
    """
    Exclui todas as tabelas
    """
    from application import models
    db.drop_all()


@manager.command
def runserver():
    """
    Inicia a aplicacao
    """
    app.run(debug=True)

if __name__ == '__main__':
    manager.run()
