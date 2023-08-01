#!/usr/bin/env python3
"""
5-app.py
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


@app.before_request
def before_request():
    """Set the global 'g.user' variable for templates
    to access the current user."""
    g.user = get_user()


@app.route('/')
def index():
    """Renders the index.html template with the translated content."""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
