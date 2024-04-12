#!/usr/bin/env python3
"""4-app.py
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Get locale
    """
    locale_params = request.args.get('locale')
    if locale_params and locale_params in app.config['LANGUAGES']:
        return locale_params
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """ Main route
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
