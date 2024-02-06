#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Class Config Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale():
    """
     detect if the incoming request contains
     locale argument and ifs value is a supported locale
    """
    locale = request.args.get('locale')
    if locale:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """ home page """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
