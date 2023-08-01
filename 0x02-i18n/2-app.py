#!/usr/bin/env python3
"""
2-app.py
"""

from flask import Flask, render_template, request
from flask_babel import Babel

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
    """Determine the best-matching language for the user."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders the index.html template with the specified content."""
    return render_template(
        '2-index.html', title="Welcome to Holberton", header="Hello world"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
