from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.database import db
from rel_bball_analytics.players.search import (
    fetch_from_api,
    get_search_result,
)

from .fixtures.dataframes import (
    expected_player_matches,
    expected_player_summary_stats,
)
from .fixtures.db_records import player_record, players_valid
from .fixtures.test_db import reset_test_db, setup_test_db


class TestGetSearchResult:
    """test suite for get_search_result"""

    @patch("rel_bball_analytics.players.search.fetch_from_api")
    def test_returns_existing_records_from_db(
        self, fetch_from_api, reset_test_db, player_record
    ):
        db.session.add(player_record)
        search_result = get_search_result(name="Curry", season="2022")

        assert type(search_result) == pd.DataFrame
        assert len(search_result) > 0
        assert not fetch_from_api.called

    @patch("rel_bball_analytics.players.search.fetch_from_api")
    def test_returns_data_from_api(self, fetch_from_api, reset_test_db, players_valid):
        fetch_from_api.return_value = pd.DataFrame(players_valid)
        search_result = get_search_result(name="Curry", season="2022")

        assert type(search_result) == pd.DataFrame
        assert len(search_result) == 2
        assert fetch_from_api.called

    @patch("rel_bball_analytics.players.search.fetch_from_api")
    def test_returns_none_if_no_matches_found(self, fetch_from_api):
        fetch_from_api.return_value = None
        search_result = get_search_result(name="Curry", season="2022")

        assert search_result is None
        assert fetch_from_api.called


class TestFetchFromApi:
    """test suite for fetch_from_api"""

    @patch("rel_bball_analytics.players.search.get_summary_stats")
    @patch("rel_bball_analytics.players.search.get_player_matches")
    def test_returns_df_with_player_profiles(
        self,
        get_player_matches,
        get_summary_stats,
        reset_test_db,
        expected_player_matches,
        expected_player_summary_stats,
    ):
        get_player_matches.return_value = expected_player_matches
        get_summary_stats.return_value = pd.DataFrame([expected_player_summary_stats])

        results = fetch_from_api(name="Curry", season=2022)

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    @patch("rel_bball_analytics.players.search.get_player_matches")
    def test_returns_none_if_no_player_matches(
        self,
        get_player_matches,
    ):
        get_player_matches.return_value = None

        results = fetch_from_api(name="Fake", season=2022)
        assert results is None

    @patch("rel_bball_analytics.players.search.get_summary_stats")
    @patch("rel_bball_analytics.players.search.get_player_matches")
    def test_returns_none_if_no_stats_available(
        self, get_player_matches, get_summary_stats, expected_player_matches
    ):
        get_player_matches.return_value = expected_player_matches
        get_summary_stats.return_value = pd.DataFrame()

        results = fetch_from_api(name="Wembanyama", season=2022)
        assert results is None
