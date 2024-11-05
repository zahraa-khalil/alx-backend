#!/usr/bin/env python3
"""i18n Module"""


from flask import Flask, render_template
from flask_babel import Babel, _, format_datetime
from datetime import datetime

app = Flask(__name__)


babel = Babel(app)


class Config:
    """language configuration"""
    LANGUAGES = ["en", "fr"]
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


if __name__ == '__main__':
    app.run(debug=True)
