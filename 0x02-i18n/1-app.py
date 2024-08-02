#!/usr/bin/env python3
"""
0x02. i18n
"""
from flask import Flask, request, render_template
from flask_babel import Babel, _


class Config:
    """Configuration class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babellocaleselector
def get_locale():
    """Gets the locale from parameter"""
    lang = request.args.get("lang")
    if lang in app.config["BABEL_SUPPORTED_LOCALES"]:
        return lang

    return request.accept_languages.best_match(
            app.config["BABEL_SUPPORTED_LOCALES"]
            )


@app.route("/")
def index():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
