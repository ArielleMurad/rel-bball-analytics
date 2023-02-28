import logging

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from .database import db


def create_app(config: str):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    db.init_app(app)
    migrate = Migrate(app, db)

    configure_db()
    configure_views(app)
    configure_logger()

    return app


def configure_db():
    from .players.models import Player

    db.create_all()


def configure_views(app: Flask):
    from .players.views import players_bp

    app.register_blueprint(players_bp)


def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s %(message)s",
    )
