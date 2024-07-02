#!/usr/bin/env python3
"""
    Module of Flask example
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
        Config class that has the supported language in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app=app)


@babel.localeselector
def get_locale():
    """
        Function that returns default locale
    """
    request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def main():
    """
        Function that renders the main page of the application
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
