#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Class Config Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def home() -> str:
    """ home page """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
