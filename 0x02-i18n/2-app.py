#!/usr/bin/env python3
"""i18n Module"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """language configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """check language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    '''default route'''
    return render_template("2-index.html",)


if __name__ == '__main__':
    app.run(debug=True)
