#!/usr/bin/env python3
from os import getenv, path
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
secrets = {}


@app.route('/dashboard', methods=["GET", "POST"])
def single_dash():
    """ The main dashboard """
    OWNER_URL = getenv("OWNER_URL", "https://thekrishna.in/")
    return render_template('dash.html.j2', OWNER_URL=OWNER_URL)


@app.route('/', methods=["GET"])
def login():
    """ Login Page """
    return render_template('login.html.j2')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def not_found(e):
    """ inbuilt function which takes error as parameter"""
    return render_template('404.html.j2')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
    print()
