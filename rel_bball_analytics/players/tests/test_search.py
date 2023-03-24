from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.players.search import get_search_result
from rel_bball_analytics.statistics.tests.fixtures.expected import player_summary_stats

from .fixtures.expected import df_player_matches


class TestGetSearchResult:
    """test suite for get_search_result"""

    @patch("rel_bball_analytics.players.search.get_summary_stats")
    @patch("rel_bball_analytics.players.search.get_player_matches")
    def test_returns_df_with_player_profiles(
        self,
        get_player_matches,
        get_summary_stats,
        df_player_matches,
        player_summary_stats,
    ):
        get_player_matches.return_value = df_player_matches
        get_summary_stats.return_value = pd.DataFrame([player_summary_stats])

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
        self, get_player_matches, get_summary_stats, df_player_matches
    ):
        get_player_matches.return_value = df_player_matches
        get_summary_stats.return_value = pd.DataFrame()

        results = get_search_result(name="Wembanyama", season=2022)
        assert results is None
