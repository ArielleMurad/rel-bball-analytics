from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.database import db
from rel_bball_analytics.players.search import (
    get_player_details,
    get_search_result,
)
from rel_bball_analytics.statistics.tests.fixtures.dataframes import (
    expected_player_summary_stats,
)

from .fixtures.database import reset_test_db, setup_test_db
from .fixtures.dataframes import expected_player_matches
from .fixtures.db_records import player_record


class TestGetSearchResult:
    """test suite for get_search_result"""

    @patch("rel_bball_analytics.players.search.get_summary_stats")
    @patch("rel_bball_analytics.players.search.get_player_matches")
    def test_returns_df_with_player_profiles(
        self,
        get_player_matches,
        get_summary_stats,
        expected_player_matches,
        expected_player_summary_stats,
    ):
        get_player_matches.return_value = expected_player_matches
        get_summary_stats.return_value = pd.DataFrame([expected_player_summary_stats])

        results = get_search_result(name="Curry", season=2022)

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    @patch("rel_bball_analytics.players.search.get_player_matches")
    def test_returns_none_if_no_player_matches(
        self,
        get_player_matches,
    ):
        get_player_matches.return_value = None

        results = get_search_result(name="Fake", season=2022)
        assert results is None

    @patch("rel_bball_analytics.players.search.get_summary_stats")
    @patch("rel_bball_analytics.players.search.get_player_matches")
    def test_returns_none_if_no_stats_available(
        self, get_player_matches, get_summary_stats, expected_player_matches
    ):
        get_player_matches.return_value = expected_player_matches
        get_summary_stats.return_value = pd.DataFrame()

        results = get_search_result(name="Wembanyama", season=2022)
        assert results is None


class TestGetPlayerDetails:
    """test suite for get_player_details"""

    @patch("rel_bball_analytics.players.search.get_player_summary_stats")
    def test_returns_player_details(
        self,
        get_player_summary_stats,
        reset_test_db,
        player_record,
        expected_player_summary_stats,
    ):
        db.session.add(player_record)
        get_player_summary_stats.return_value = expected_player_summary_stats

        results = get_player_details(id=124, season=2022)

        assert results["season"] == 2022
        assert results["firstname"] == "Stephen"
        assert results["lastname"] == "Curry"
        assert results["team"] == ["GSW"]
        assert results["games_played"] == 2
        assert results["points"] == 25
