#!/usr/bin/env python3
"""5-app.py

This module contains a Flask application that demonstrates internationalization
(i18n) and localization (l10n) using Flask-Babel.

The application allows users to view the index page in different languages
based on their preferences.

The available languages in the application are
English ('en') and French ('fr').

The application also provides a way to simulate logging in as different
users by specifying the 'login_as' query parameter.

The user information is stored in a dictionary called 'users'.

The application uses Flask-Babel for i18n and l10n.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config class for Flask app configuration."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the user based on the 'login_as' query parameter.

    Returns:
        The user object if the 'login_as' parameter is valid and corresponds to
        a user in the 'users' dictionary.
        None if the 'login_as' parameter is not provided or does not correspond
        to a user in the 'users' dictionary.
    """
    id = request.args.get('login_as')
    if id is not None and int(id) in users.keys():
        return users[int(id)]
    return None


@app.before_request
def before_request():
    """
    Function to be executed before each request.
    It retrieves the user and assigns it to the global 'g' object.
    """
    user = get_user()
    g.user = user


def get_locale() -> str:
    """Get the locale based on the 'locale' query parameter or the
    'accept_languages' header.

    Returns:
        The best matching locale from the available languages in the app
        configuration.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app)


@app.route('/')
def index():
    """Render the index template."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port='5000', host='127.0.0.1', debug=True)
