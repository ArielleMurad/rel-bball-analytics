import logging

from dotenv import load_dotenv
from flask import Flask

from .database import db, migrate


def create_app(config: str):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()

    db.init_app(app)
    migrate.init_app(app, db)

    configure_db()
    configure_views(app)
    configure_logger()

    return app


def configure_db():
    from .games.models import Game
    from .players.models import Player
    from .statistics.models import Statistic

    db.create_all()


def configure_views(app: Flask):
    from .players.views import players_bp

    app.register_blueprint(players_bp)


def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s %(message)s",
    )
