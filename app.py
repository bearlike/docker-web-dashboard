#!/usr/bin/env python3
import os
from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
secrets = {}


@app.route('/', methods=["GET"])
def single_dash():
    """ The main dashboard """
    return render_template('index.html.j2')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')



@app.errorhandler(404)
def not_found(e):
    """ inbuilt function which takes error as parameter"""
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
    print()