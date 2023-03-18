from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.statistics.data_source import (
    clean_stats_data,
    get_player_summary_stats,
    get_summary_stats,
)

from ...players.tests.fixtures.api_responses import (
    empty_response,
    stats_full,
    stats_missing,
)
from ...players.tests.fixtures.dataframes import (
    expected_clean_stats_data,
    expected_player_summary_stats,
)


class TestGetSummaryStats:
    """test suite for get_summary_stats"""

    @patch("rel_bball_analytics.players.summary_stats.get_data_from_api")
    def test_returns_summary_stats(self, get_data_from_api, stats_full):
        get_data_from_api.return_value = stats_full
        results = get_summary_stats(player_ids=[124], season=2022)

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    @patch("rel_bball_analytics.players.summary_stats.get_data_from_api")
    def test_returns_empty_df_if_no_stats(self, get_data_from_api, empty_response):
        get_data_from_api.return_value = empty_response
        results = get_summary_stats(player_ids=[000], season=2022)

        assert type(results) == pd.DataFrame
        assert results.empty

    @patch("rel_bball_analytics.players.summary_stats.get_data_from_api")
    def test_returns_empty_df_if_missing_stats(self, get_data_from_api, stats_missing):
        get_data_from_api.return_value = stats_missing
        results = get_summary_stats(player_ids=[121], season=2022)

        assert type(results) == pd.DataFrame
        assert results.empty


class TestCleanStatsData:
    """test suite for clean_stats_data"""

    def test_returns_formatted_stats_data(self, stats_full, expected_clean_stats_data):
        stats = pd.DataFrame(stats_full["response"])
        results = clean_stats_data(stats=stats)

        assert results.equals(expected_clean_stats_data)

    def test_returns_none_if_missing_data(self, stats_missing):
        stats = pd.DataFrame(stats_missing["response"])
        results = clean_stats_data(stats=stats)

        assert results is None


class TestGetPlayerSummaryStats:
    """test suite for get_player_summary_stats"""

    def test_returns_summary_stats(
        self, expected_clean_stats_data, expected_player_summary_stats
    ):
        results = get_player_summary_stats(
            id=124, season=2022, stats=expected_clean_stats_data
        )

        assert results == expected_player_summary_stats
