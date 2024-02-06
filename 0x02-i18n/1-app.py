#!/usr/bin/env python3
"""
    This Module contains a basic api route
    Author: Peter Ekwere
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config:
    """ Config class
    """
    LANGUAGES = ["en", "fr"]


@app.route('/')
def index():
    """ an index endpoint
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)