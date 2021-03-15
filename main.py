#!/usr/bin/env python3
from database import Connection
from os import getenv, path
from flask import Flask, request, render_template, send_from_directory, redirect, url_for

app = Flask(__name__)


DASH_USERNAME = getenv("DASH_USERNAME", "admin")
DASH_PASSWORD = getenv("DASH_PASSWORD", "admin")
OWNER_URL = getenv("OWNER_URL", "https://thekrishna.in/")
secrets = {}


def validate_login(username=None, password=None):
    """ Validate Credentials """
    # False if Invalid Credentials
    return bool(username == DASH_USERNAME and password == DASH_PASSWORD)


@app.route('/add-site', methods=["GET", "POST"])
def add_site():
    """ Add new site form """
    # db = Connection(app)
    return render_template('add-site.html.j2')


@app.route('/dashboard', methods=["GET", "POST"])
def single_dash():
    """ The main dashboard """
    db = Connection(app)
    is_auth = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_auth = validate_login(username, password)
    if is_auth is False:
        return redirect(url_for('login', error=True))
    data = db.get_sites()
    return render_template('dash.html.j2', DASH=data, OWNER_URL=OWNER_URL)


@app.route('/', methods=["GET"])
def login():
    """ Login Page """
    error = request.args.get('error')
    return render_template('login.html.j2', error=error)


@app.route('/favicon.ico')
def favicon():
    """ Send Favicon to Clients """
    return send_from_directory(path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def not_found(e):
    """ inbuilt function which takes error as parameter"""
    return render_template('404.html.j2')


if __name__ == '__main__':
    print("\n=============\n")
    app.run(host='127.0.0.1', port=8081, debug=True)
