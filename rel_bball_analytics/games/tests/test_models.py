from rel_bball_analytics.database import db, delete_records, fetch_records, save_records
from rel_bball_analytics.games.models import Game

from .fixtures.database import reset_test_db, setup_test_db
from .fixtures.db_records import (
    game_record,
    games_duplicate,
    games_missing_required_field,
    games_valid,
)


class TestSaveGameRecords:
    """test suite for save_records"""

    def test_saves_stats_data_to_db(self, reset_test_db, games_valid):
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


# class TestFetchGameRecords:
#     """test suite for fetch_records"""

#     def test_returns_records_matching_query(self, reset_test_db, stats_record):
#         db.session.add(stats_record)
#         records = fetch_records(model=Game, season=2022, home=2022)

#         assert len(records) > 0
#         assert records[0]["id"] == "124_10101"
#         assert records[0]["team"] == "GSW"
#         assert records[0]["position"] == "PG"
#         assert records[0]["points"] == 25
#         assert records[0]["minutes_played"] == 27

#     def test_returns_empty_list_if_no_matches(self, reset_test_db, stats_record):
#         db.session.add(stats_record)
#         records = fetch_records(model=Game, player_id=265, season=2019)

#         assert len(records) == 0


# class TestDeleteGameRecords:
#     """test suite for delete_records"""

#     def test_deletes_all_records_matching_query(self, reset_test_db, game_record):
#         db.session.add(game_record)
#         delete_records(model=Game, player_id=124, season=2022)

#         records = db.session.query(Game).all()
#         assert len(records) == 0

#     def test_deletes_none_if_no_records_match_query(self, reset_test_db, stats_record):
#         db.session.add(stats_record)
#         delete_records(model=Game, player_id=265, season=2019)

#         records = db.session.query(Game).all()
#         assert len(records) > 0
