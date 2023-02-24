import logging

from dotenv import load_dotenv
from flask import Flask, render_template

from .players.views import players_bp

load_dotenv()

app = Flask(__name__)

app.config.from_pyfile("settings.py")
app.logger.setLevel(logging.INFO)

app.register_blueprint(players_bp)


@app.route("/")
def home():
    return render_template("home.html")
