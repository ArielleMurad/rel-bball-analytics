from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.games.data_source import (
    clean_game_data,
    fetch_game_data,
    filter_finished_games,
    get_game_stats,
)
from rel_bball_analytics.tests.fixtures.database import reset_test_db, setup_test_db

from .fixtures.api_responses import (
    empty_response,
    games_finished,
    games_unfinished,
)
from .fixtures.expected import df_game_data


class TestGetGameStats:
    """test suite for get_game_stats"""

    @patch("rel_bball_analytics.games.data_source.fetch_game_data")
    def test_returns_dataframe_with_stats_data(
        self, fetch_game_data, reset_test_db, df_game_data
    ):
        fetch_game_data.return_value = df_game_data
        result = get_game_stats(team_id=11, team="GSW", season=2022)

        assert type(result) == pd.DataFrame
        assert len(result) > 0

        assert result.iloc[0]["id"] == 1
        assert result.iloc[1]["id"] == 2

    @patch("rel_bball_analytics.games.data_source.fetch_game_data")
    def test_returns_none_if_no_matches_found(self, fetch_game_data):
        fetch_game_data.return_value = None
        result = get_game_stats(team_id=00, team="Fake", season=2022)

        assert result is None


class TestFetchGameData:
    """test suite for fetch_game_data"""

    @patch("rel_bball_analytics.games.data_source.get_data_from_api")
    def test_returns_dataframe_for_valid_matches(
        self, get_data_from_api, games_finished
    ):
        get_data_from_api.return_value = games_finished
        results = fetch_game_data(team_id=11, season=2022)

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    @patch("rel_bball_analytics.games.data_source.get_data_from_api")
    def test_returns_none_if_no_matches(self, get_data_from_api, empty_response):
        get_data_from_api.return_value = empty_response
        results = fetch_game_data(team_id=00, season=2022)

        assert results is None

    @patch("rel_bball_analytics.games.data_source.get_data_from_api")
    def test_returns_none_if_no_finished_games(
        self, get_data_from_api, games_unfinished
    ):
        get_data_from_api.return_value = games_unfinished
        results = fetch_game_data(team_id=17, season=2022)

        assert results is None


class TestFilterFinishedGames:
    """test suite for filter_finished_games"""

    def test_returns_finished_games(self, games_finished):
        games = pd.DataFrame(games_finished["response"])
        results = filter_finished_games(games=games)

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    def test_returns_empty_df_if_no_finished_games(self, games_unfinished):
        games = pd.DataFrame(games_unfinished["response"])
        results = filter_finished_games(games=games)

        assert type(results) == pd.DataFrame
        assert results.empty


class TestCleanGameData:
    """test suite for clean_game_data"""

    def test_returns_formatted_game_data(self, games_finished, df_game_data):
        games = pd.DataFrame(games_finished["response"])
        results = clean_game_data(games=games)

        assert results.equals(df_game_data)
