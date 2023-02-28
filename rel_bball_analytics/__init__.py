from flask import render_template

from .setup import create_app

app = create_app(config="rel_bball_analytics.config.DevelopmentConfig")


@app.route("/")
def home():
    return render_template("home.html")
