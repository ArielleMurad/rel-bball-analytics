from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.statistics.summary import (
    get_player_summary_stats,
    get_summary_stats,
)

from .fixtures.dataframes import (
    expected_clean_stats_data,
    expected_player_stats,
    expected_player_summary_stats,
)


class TestGetSummaryStats:
    """test suite for get_summary_stats"""

    @patch("rel_bball_analytics.statistics.summary.get_player_stats")
    def test_returns_summary_stats(self, get_player_stats, expected_player_stats):
        get_player_stats.return_value = expected_player_stats
        results = get_summary_stats(player_ids=[124], season=2022)

        assert type(results) == pd.DataFrame
        assert len(results) == 1

    @patch("rel_bball_analytics.statistics.summary.get_player_stats")
    def test_returns_empty_df_if_no_stats(self, get_player_stats):
        get_player_stats.return_value = None
        results = get_summary_stats(player_ids=[000], season=2022)

        assert type(results) == pd.DataFrame
        assert results.empty


class TestGetPlayerSummaryStats:
    """test suite for get_player_summary_stats"""

    def test_returns_player_summary_stats(
        self, expected_player_stats, expected_player_summary_stats
    ):
        results = get_player_summary_stats(stats=expected_player_stats)

        assert results == expected_player_summary_stats
