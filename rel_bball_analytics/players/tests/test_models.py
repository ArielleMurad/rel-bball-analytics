from rel_bball_analytics.database import db, fetch_records, save_records
from rel_bball_analytics.players.models import Player
from rel_bball_analytics.tests.fixtures.database import reset_test_db, setup_test_db

from .fixtures.db_records import (
    player_record,
    players_duplicate,
    players_missing_required_field,
    players_valid,
)


class TestSavePlayerRecords:
    """test suite for save_records"""

    def test_saves_player_data_to_db(self, reset_test_db, players_valid):
        save_records(model=Player, items=players_valid)
        records = db.session.query(Player).all()

        assert len(records) == 2

    def test_missing_required_data(self, players_missing_required_field):
        save_records(model=Player, items=players_missing_required_field)
        records = db.session.query(Player).all()

        assert len(records) == 0

    def test_duplicate_records(self, players_duplicate):
        save_records(model=Player, items=players_duplicate)
        records = db.session.query(Player).all()

        assert len(records) == 0


class TestFetchPlayerRecords:
    """test suite for fetch_records"""

    def test_returns_records_matching_query(self, reset_test_db, player_record):
        db.session.add(player_record)
        records = fetch_records(model=Player, lastname="Curry")

        assert len(records) > 0
        assert records[0]["id"] == 124
        assert records[0]["firstname"] == "Stephen"
        assert records[0]["lastname"] == "Curry"

    def test_returns_empty_list_if_no_matches(self, reset_test_db, player_record):
        db.session.add(player_record)
        records = fetch_records(model=Player, lastname="James")

        assert len(records) == 0
