#!/usr/bin/env python3
"""
app.py
"""

from flask import Flask, render_template, g, request
from flask_babel import Babel, _, get_locale, timezone_selector
import pytz
from datetime import datetime

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


@babel.timezoneselector
def get_timezone():
    """Determine the best-matching timezone for the user.

    The order of priority is:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default to UTC
    """
    # 1. Timezone from URL parameters
    if 'timezone' in request.args:
        timezone = request.args['timezone']
        try:
            pytz.timezone(timezone)  # Validate if the timezone is valid
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 2. Timezone from user settings
    user = get_user()
    if user and user['timezone']:
        try:
            pytz.timezone(user['timezone'])  # Validate if the timezone
            return user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 3. Default to UTC
    return 'UTC'


@app.before_request
def before_request():
    """Set the global 'g.user' and 'g.timezone' variables
    for templates to access."""
    g.user = get_user()
    g.timezone = get_timezone()


@app.route('/')
def index():
    """Renders the index.html template with the translated content."""
    current_time = datetime.now(
      pytz.timezone(g.timezone)).strftime("%b %d, %Y, %I:%M:%S %p")
    welcome_message = _(
      "logged_in_as", username=g.user['name']
    ) if g.user else _("not_logged_in")
    time_message = _("current_time_is", current_time=current_time)
    return render_template(
      'index.html', welcome_message=welcome_message, time_message=time_message
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
