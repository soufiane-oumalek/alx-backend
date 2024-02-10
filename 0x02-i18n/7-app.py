#!/usr/bin/env python3
""" Use user locale
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz


app = Flask(__name__)
babel = Babel(app)
"""Babel object """
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" class as config for Flask app """


def get_user():
    """ returns a user dictionary or None
    """
    return users["id"] if id is not None else None


@babel.localeselector
def get_locale():
    """ the best match with our supported languages """
    localLang = request.args.get('locale')
    supportLang = app.config['LANGUAGES']
    if localLang in supportLang:
        return localLang
    userId = request.args.get('login_as')
    if userId:
        localLang = users[int(userId)]['locale']
        if localLang in supportLang:
            return localLang
    localLang = request.headers.get('locale')
    if localLang in supportLang:
        return localLang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """ use get_user to find a user if """
    g.user = get_user()


@app.route('/')
def home() -> str:
    """ home page """
    return render_template('6-index.html')


@babel.timezoneselector
def get_timezone():
    """ Infer appropriate time zone """
    localTimezone = request.args.get('timezone')
    if localTimezone in pytz.all_timezones:
        return localTimezone
    else:
        raise pytz.exceptions.UnknownTimeZoneError
    userId = request.args.get('login_as')
    localTimezone = users[int(userId)]['timezone']
    if localTimezone in pytz.all_timezones:
        return localTimezone
    else:
        raise pytz.exceptions.UnknownTimeZoneError
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
