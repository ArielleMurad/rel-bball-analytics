import pytest

from rel_bball_analytics.database import db
from rel_bball_analytics.players.models import (
    Player,
    fetch_player_records,
    save_player_records,
)

from .fixtures.db_records import (
    player_record,
    players_duplicate,
    players_missing_required_field,
    players_valid,
)
from .fixtures.test_db import reset_test_db, setup_test_db


class TestSavePlayerRecords:
    """test suite for save_player_records"""

    def test_saves_player_data_to_db(self, reset_test_db, players_valid):
        save_player_records(players=players_valid)
        records = db.session.query(Player).all()

        assert len(records) == 2

    def test_missing_required_data(self, players_missing_required_field):
        save_player_records(players=players_missing_required_field)
        records = db.session.query(Player).all()

        assert len(records) == 0

    def test_duplicate_records(self, players_duplicate):
        save_player_records(players=players_duplicate)
        records = db.session.query(Player).all()

        assert len(records) == 0


class TestFetchPlayerRecords:
    """test suite for fetch_player_records"""

    def test_returns_records_matching_query(self, reset_test_db, player_record):
        db.session.add(player_record)
        records = fetch_player_records(lastname="Curry", season=2022)

        assert len(records) > 0
        assert records[0]["id"] == "124_2022"
        assert records[0]["firstname"] == "Stephen"
        assert records[0]["lastname"] == "Curry"
        assert records[0]["season"] == 2022

    def test_returns_empty_list_if_no_matches(self, reset_test_db, player_record):
        db.session.add(player_record)
        records = fetch_player_records(lastname="James", season=2022)

        assert len(records) == 0
