#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Bable

app = Flask(__name__)
babel = Bable(app)
"""Babel object"""


class config(object):
    """ class config """
    LANGUAGES = ['en', 'fr']
    BABLE_DEFAULT_LOCATE = 'en'
    BABLE_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
"""config for flask app"""

@app.route('/')
def home():
    """ home page """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
