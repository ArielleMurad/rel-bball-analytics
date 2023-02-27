from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")

SPORTS_API_URL = environ.get("SPORTS_API_URL")
SPORTS_API_KEY = environ.get("SPORTS_API_KEY")


def configure_db(db: SQLAlchemy):
    from .players.models import Player

    db.create_all()


def configure_views(app: Flask):
    from .players.views import players_bp

    app.register_blueprint(players_bp)
