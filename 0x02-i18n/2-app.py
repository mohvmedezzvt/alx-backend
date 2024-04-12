#!/usr/bin/env python3
"""2-app.py

This module contains a Flask application that supports
internationalization (i18n).
It uses Flask-Babel extension to handle translations and localization.

The application defines a Config class that holds the configuration
settings for the application.
"""

from flask import Flask, render_template
from flask_babel import Babel
from flask import request


class Config(object):
    """Config class

    This class holds the configuration settings for the Flask application.
    It defines the supported languages, default locale, and default timezone.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale

    This function determines the best matching language based
    on the user's preferences.
    It is used as the locale selector for Flask-Babel.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Main route

    This route renders the index template.

    Returns:
        str: The rendered template.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
