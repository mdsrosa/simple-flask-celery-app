# -*- coding: utf-8 -*-
__author__ = 'matheusrosa'
import sqlite3
from flask import Flask, g, request, session, redirect, url_for, flash, abort, \
    render_template

app = Flask(__name__)
app.config.from_object('settings')


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
        with app.open_resource('schema.sql', mode='r') as f:
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


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id asc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries,
                           title=u'My Entries')


@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted.')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in')
    flash('You were logged out.')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
