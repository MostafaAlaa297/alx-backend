#!/usr/bin/env python3
"""
0x02. i18n
"""
from flask import Flask, request, render_template
from flask_babel import Babel, _

app = Flask(__name__)
app.config["BABEL_DEFAULT_LOCALE"] = "en"
app.config["BABEL_DEFAULT_TIMEZONE"] = "UTC"
app.config["BABEL_SUPPORTED_LOCALES"] = ["en", "fr"]
babel = Babel(app)


@babellocaleselector
def get_locale():
    """Gets the locale from parameter"""
    lang = request.args.get("lang")
    if lang in app.config["BABEL_SUPPORTED_LOCALES"]:
        return lang

    return request.accept_languages.best_match(app.config["BABEL_SUPPORTED_LOCALES"])


@app.route("/")
def index():
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
