#!/usr/bin/env python3
"""
4-app.py
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_locale

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class for available languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the best-matching language for the user.

    If the `locale` parameter is provided in the request's query
    string and is a
    supported locale, return it. Otherwise, use the default behavior.
    """
    if 'locale' in request.args and \
        request.args['locale'] in app.config['LANGUAGES']:

        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Set the global `g.locale` variable for templates
    to access the current locale."""
    g.locale = str(get_locale())


@app.route('/')
def index():
    """Renders the index.html template with the translated content."""
    return render_template(
        '4-index.html', title=_("home_title"), header=_("home_header")
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
