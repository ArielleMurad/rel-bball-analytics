import pytest

from rel_bball_analytics.database import db
from rel_bball_analytics.players.models import Player
from rel_bball_analytics.setup import create_app


@pytest.fixture(scope="module", autouse=True)
def setup_test_db():
    create_app(config="rel_bball_analytics.config.TestingConfig")

    yield

    db.session.rollback()
    db.session.close()


@pytest.fixture()
def reset_test_db():
    yield

    db.session.query(Player).delete()
    db.session.commit()
