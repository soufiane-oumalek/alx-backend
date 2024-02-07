#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Class Config Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


def get_user() -> Union[Dict, None]:
    """Retrieves a user
    """
    id_log = request.args.get('login_as')
    if id_log:
        return users.get(int(id_log))
    return None


@app.before_request
def before_request() -> None:
    """ use get_user to find a user """
    g.user = get_user


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
