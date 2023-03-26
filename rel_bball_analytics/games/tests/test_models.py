from rel_bball_analytics.database import db, delete_records, fetch_records, save_records
from rel_bball_analytics.games.models import Game
from rel_bball_analytics.tests.fixtures.database import reset_test_db, setup_test_db

from .fixtures.db_records import (
    game_records,
    games_duplicate,
    games_missing_required_field,
    games_valid,
)


class TestSaveGameRecords:
    """test suite for save_records"""

    def test_saves_game_data_to_db(self, reset_test_db, games_valid):
        save_records(model=Game, items=games_valid)
        records = db.session.query(Game).all()

        assert len(records) == 2

    def test_missing_required_data(self, games_missing_required_field):
        save_records(model=Game, items=games_missing_required_field)
        records = db.session.query(Game).all()

        assert len(records) == 0

    def test_duplicate_records(self, games_duplicate):
        save_records(model=Game, items=games_duplicate)
        records = db.session.query(Game).all()

        assert len(records) == 0


class TestFetchGameRecords:
    """test suite for fetch_records"""

    def test_returns_records_matching_query(self, reset_test_db, game_records):
        db.session.add_all(game_records)
        or_clause = {"home": "GSW", "away": "GSW"}
        records = fetch_records(model=Game, or_clause=or_clause, season=2022)

        assert len(records) == 2
        assert records[0]["id"] == 1
        assert records[0]["winner"] == "GSW"
        assert records[1]["id"] == 2
        assert records[1]["winner"] == "DEN"

    def test_returns_empty_list_if_no_matches(self, reset_test_db, game_records):
        db.session.add_all(game_records)
        or_clause = {"home": "LAL", "away": "LAL"}
        records = fetch_records(model=Game, or_clause=or_clause, season=2019)

        assert len(records) == 0


class TestDeleteGameRecords:
    """test suite for delete_records"""

    def test_deletes_all_records_matching_query(self, reset_test_db, game_records):
        db.session.add_all(game_records)
        or_clause = {"home": "GSW", "away": "GSW"}
        delete_records(model=Game, or_clause=or_clause, season=2022)

        records = db.session.query(Game).all()
        assert len(records) == 0

    def test_deletes_none_if_no_records_match_query(self, reset_test_db, game_records):
        db.session.add_all(game_records)
        or_clause = {"home": "LAL", "away": "LAL"}
        delete_records(model=Game, or_clause=or_clause, season=2022)

        records = db.session.query(Game).all()
        assert len(records) > 0
