from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.statistics.data_source import (
    clean_stats_data,
    fetch_stats_data,
    get_player_stats,
)

from .fixtures.api_responses import empty_response, stats_full, stats_missing
from .fixtures.database import reset_test_db, setup_test_db
from .fixtures.expected import df_stats_data


class TestGetPlayerStats:
    """test suite for get_player_stats"""

    @patch("rel_bball_analytics.statistics.data_source.fetch_stats_data")
    def test_returns_dataframe_with_stats_data(
        self, fetch_stats_data, reset_test_db, df_stats_data
    ):
        fetch_stats_data.return_value = df_stats_data
        result = get_player_stats(player_id=124, season=2022)

        assert type(result) == pd.DataFrame
        assert len(result) > 0

        assert result.iloc[0]["id"] == "124_1"
        assert result.iloc[0]["player_id"] == 124
        assert result.iloc[0]["season"] == 2022

    @patch("rel_bball_analytics.statistics.data_source.fetch_stats_data")
    def test_returns_none_if_no_matches_found(self, fetch_stats_data):
        fetch_stats_data.return_value = None
        result = get_player_stats(player_id=000, season=2022)

        assert result is None


class TestFetchStatsData:
    """test suite for fetch_stats_data"""

    @patch("rel_bball_analytics.statistics.data_source.get_data_from_api")
    def test_returns_dataframe_for_valid_matches(self, get_data_from_api, stats_full):
        get_data_from_api.return_value = stats_full
        results = fetch_stats_data(player_id=124, season=2022)

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    @patch("rel_bball_analytics.statistics.data_source.get_data_from_api")
    def test_returns_none_if_no_matches(self, get_data_from_api, empty_response):
        get_data_from_api.return_value = empty_response
        results = fetch_stats_data(player_id=000, season=2022)

        assert results is None

    @patch("rel_bball_analytics.statistics.data_source.get_data_from_api")
    def test_returns_empty_df_if_missing_stats(self, get_data_from_api, stats_missing):
        get_data_from_api.return_value = stats_missing
        results = fetch_stats_data(player_id=121, season=2022)

        assert results is None


class TestCleanStatsData:
    """test suite for clean_stats_data"""

    def test_returns_formatted_stats_data(self, stats_full, df_stats_data):
        stats = pd.DataFrame(stats_full["response"])
        results = clean_stats_data(stats=stats)

        assert results.equals(df_stats_data)

    def test_returns_none_if_missing_data(self, stats_missing):
        stats = pd.DataFrame(stats_missing["response"])
        results = clean_stats_data(stats=stats)

        assert results is None
