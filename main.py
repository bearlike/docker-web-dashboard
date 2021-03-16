#!/usr/bin/env python3
from flask import Flask, redirect, request, render_template, send_from_directory, \
    session, url_for
from database import Connection
from os import getenv, path
from werkzeug.utils import secure_filename
import uuid


app = Flask(__name__)
app.secret_key = 'C#hMq5w#52NaM@Nz'


DASH_USERNAME = getenv("DASH_USERNAME", "admin")
DASH_PASSWORD = getenv("DASH_PASSWORD", "admin")
OWNER_URL = getenv("OWNER_URL", "https://thekrishna.in/")
secrets = {}


def validate_login(username=None, password=None):
    """ Validate Credentials """
    # False if Invalid Credentials
    return bool(username == DASH_USERNAME and password == DASH_PASSWORD)


@app.route('/form/add-site', methods=["POST"])
def form_add_site():
    """ Handle Add POST """
    status = False
    db = Connection(app)
    # During Testing
    # db = Connection(app, host="kry-server.local")
    if request.method == 'POST':
        # Form Variables
        app_title = request.form['app_title']
        colour_hex = request.form['colour_hex']
        app_url = request.form['app_url']
        groups = request.form['groups']
        # File Handling
        f = request.files['file']
        new_filename = secure_filename(
            str(uuid.uuid4()) + "." + f.filename.split(".")[1])
        f.save(path.join("static/logos", new_filename))
        db.add_site(groups, app_title, colour_hex, app_url, new_filename)
        status = True
    return redirect(url_for('add_site', success=status))


@app.route('/add-site', methods=["GET", "POST"])
def add_site(success=False):
    """ Add new site form """
    success = request.args.get('success')
    return render_template('add-site.html.j2', success=success)


@app.route('/dashboard', methods=["GET", "POST"])
def single_dash():
    """ The main dashboard """
    db = Connection(app)
    # db = Connection(app, host="kry-server.local")
    is_auth = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_auth = validate_login(username, password)
    elif 'dash_username' in session and 'dash_password' in session:
        username = session['dash_username']
        password = session['dash_password']
        is_auth = validate_login(username, password)
    if is_auth is False:
        return redirect(url_for('login', error=True))
    session['dash_username'] = username
    session['dash_password'] = password
    data = db.get_sites()
    return render_template('dash.html.j2', DASH=data, OWNER_URL=OWNER_URL)


@app.route('/', methods=["GET"])
def login():
    """ Login Page """
    session.pop('dash_username', None)
    session.pop('dash_password', None)
    error = request.args.get('error')
    return render_template('login.html.j2', error=error)


@app.route('/favicon.ico')
def favicon():
    """ Send Favicon to Clients """
    return send_from_directory(path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def not_found(e):
    """ inbuilt function which takes error as parameter"""
    return render_template('404.html.j2')


if __name__ == '__main__':
    print("\n", "="*8, "\n")
    app.run(host='127.0.0.1', port=8081, debug=True)
