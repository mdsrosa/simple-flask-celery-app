__author__ = 'matheusrosa'
from flask import session, request, abort, flash, render_template, redirect, \
    url_for
from application import app, get_db
from application.tasks import add_entry_task


@app.route('/')
def show_entries():
    """
    Lista todos os posts
    :return:
    """
    db = get_db()
    cur = db.execute('select title, text from entries order by id asc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries,
                           title=u'My Entries')


@app.route('/add', methods=['POST'])
def add_entry():
    """
    View para adicionar o novo post assincronamente
    utilizando a task 'add_new_entry_task'
    :return: function
    """
    if not session.get('logged_in'):
        abort(401)
    flash('New entry will be processed before saving.')
    add_entry_task.apply_async((request.form['title'], request.form['text']))
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    View que ira fazer a renderizacao do template do login
    como tambem fazer a autenticacao
    :return: function
    """
    error = None
    import ipdb; ipdb.set_trace()  # BREAKPOINT
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
    """
    View para deslogar o usuario
    :return: function
    """
    session.pop('logged_in')
    flash('You were logged out.')
    return redirect(url_for('show_entries'))
