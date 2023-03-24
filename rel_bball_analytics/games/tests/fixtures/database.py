import pytest

from rel_bball_analytics.database import db
from rel_bball_analytics.games.models import Game
from rel_bball_analytics.setup import create_app
from rel_bball_analytics.statistics.models import Statistic


@pytest.fixture(scope="module", autouse=True)
def setup_test_db():
    create_app(config="rel_bball_analytics.config.TestingConfig")

    yield

    db.session.rollback()
    db.session.close()


@pytest.fixture()
def reset_test_db():
    yield

    db.session.query(Game).delete()
    db.session.query(Statistic).delete()
    db.session.commit()
