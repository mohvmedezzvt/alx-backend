from flask import Flask, render_template, request, g
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
        The user object if the 'login_as' parameter is valid and corresponds to a user in the 'users' dictionary.
        None if the 'login_as' parameter is not provided or does not correspond to a user in the 'users' dictionary.
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
    """ Get locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app)


@app.route('/')
def index():
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
