#!/usr/bin/env python3
""" Flask app, Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class config(object):
    """ class config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCATE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
"""config for flask app"""

@app.route('/', strict_slashes=False)
def home() -> str:
    """ home page """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
