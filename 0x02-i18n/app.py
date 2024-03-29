#!/usr/bin/env python3
"""
    This Module contains a basic api route
    Author: Peter Ekwere
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ an index endpoint
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
