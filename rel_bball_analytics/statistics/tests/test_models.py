from rel_bball_analytics.database import db, delete_records, fetch_records, save_records
from rel_bball_analytics.statistics.models import Statistic
from rel_bball_analytics.tests.fixtures.database import reset_test_db, setup_test_db

from .fixtures.db_records import (
    stats_duplicate,
    stats_missing_required_field,
    stats_record,
    stats_valid,
)


class TestSaveStatisticRecords:
    """test suite for save_records"""

    def test_saves_stats_data_to_db(self, reset_test_db, stats_valid):
        save_records(model=Statistic, items=stats_valid)
        records = db.session.query(Statistic).all()

        assert len(records) == 2

    def test_missing_required_data(self, stats_missing_required_field):
        save_records(model=Statistic, items=stats_missing_required_field)
        records = db.session.query(Statistic).all()

        assert len(records) == 0

    def test_duplicate_records(self, stats_duplicate):
        save_records(model=Statistic, items=stats_duplicate)
        records = db.session.query(Statistic).all()

        assert len(records) == 0


class TestFetchStatisticRecords:
    """test suite for fetch_records"""

    def test_returns_records_matching_query(self, reset_test_db, stats_record):
        db.session.add(stats_record)
        records = fetch_records(model=Statistic, player_id=124, season=2022)

        assert len(records) > 0
        assert records[0]["id"] == "124_1"
        assert records[0]["team"] == "GSW"
        assert records[0]["position"] == "PG"
        assert records[0]["points"] == 25
        assert records[0]["minutes_played"] == 27

    def test_returns_empty_list_if_no_matches(self, reset_test_db, stats_record):
        db.session.add(stats_record)
        records = fetch_records(model=Statistic, player_id=265, season=2019)

        assert len(records) == 0


class TestDeleteStatisticRecords:
    """test suite for delete_records"""

    def test_deletes_all_records_matching_query(self, reset_test_db, stats_record):
        db.session.add(stats_record)
        delete_records(model=Statistic, player_id=124, season=2022)

        records = db.session.query(Statistic).all()
        assert len(records) == 0

    def test_deletes_none_if_no_records_match_query(self, reset_test_db, stats_record):
        db.session.add(stats_record)
        delete_records(model=Statistic, player_id=265, season=2019)

        records = db.session.query(Statistic).all()
        assert len(records) > 0
