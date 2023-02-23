from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.players.player_search import player_search

from .fixtures.dataframes import (
    expected_player_matches,
    expected_player_summary_stats,
)


class TestPlayerSearch:
    """test suite for player_search"""

    @patch("rel_bball_analytics.players.player_search.get_summary_stats")
    @patch("rel_bball_analytics.players.player_search.get_player_matches")
    def test_returns_df_with_player_profiles(
        self,
        get_player_matches,
        get_summary_stats,
        expected_player_matches,
        expected_player_summary_stats,
    ):
        get_player_matches.return_value = expected_player_matches
        get_summary_stats.return_value = pd.DataFrame([expected_player_summary_stats])

        results = player_search(name="Curry")

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    @patch("rel_bball_analytics.players.player_search.get_player_matches")
    def test_returns_none_if_no_player_matches(
        self,
        get_player_matches,
    ):
        get_player_matches.return_value = None

        results = player_search(name="Fake")
        assert results is None

    @patch("rel_bball_analytics.players.player_search.get_summary_stats")
    @patch("rel_bball_analytics.players.player_search.get_player_matches")
    def test_returns_none_if_no_stats_available(
        self, get_player_matches, get_summary_stats, expected_player_matches
    ):
        get_player_matches.return_value = expected_player_matches
        get_summary_stats.return_value = pd.DataFrame()

        results = player_search(name="Wembanyama")
        assert results is None
