#!/usr/bin/env python3
"""
6-app.py
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _, get_locale

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Return the user dictionary based on
    the 'login_as' parameter or None if not found."""
    user_id = request.args.get('login_as', type=int)
    if user_id in users:
        return users[user_id]
    return None


def get_locale():
    """Determine the best-matching language for the user.

    The order of priority is:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    # 1. Locale from URL parameters
    if 'locale' in request.args and
  request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']

    # 2. Locale from user settings
    user = get_user()
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']

    # 3. Locale from request header
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request():
    """Set the global 'g.user' and 'g.locale' variables
    for templates to access."""
    g.user = get_user()
    g.locale = get_locale()


@app.route('/')
def index():
    """Renders the index.html template with the translated content."""
    welcome_message = _(
      "logged_in_as", username=g.user['name']
    ) if g.user else _("not_logged_in")
    return render_template(
      '6-index.html', welcome_message=welcome_message
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
