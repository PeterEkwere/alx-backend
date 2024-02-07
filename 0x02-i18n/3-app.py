#!/usr/bin/env python3
"""
    This Module contains a basic api route
    Author: Peter Ekwere
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config class
    """
    LANGUAGES = ["en", "fr"]
    BABELS_DEFAULT_locale = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ This function determines the best match with our supported languages.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """ an index endpoint
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
