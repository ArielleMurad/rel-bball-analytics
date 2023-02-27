import logging

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from .settings import configure_db

load_dotenv()

app = Flask(__name__)
app.app_context().push()

app.config.from_pyfile("settings.py")
app.logger.setLevel(logging.INFO)

db = SQLAlchemy(app)
configure_db(db=db)


@app.route("/")
def index():
    return render_template("index.html")
