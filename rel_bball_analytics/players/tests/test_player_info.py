from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.players.player_info import (
    clean_player_data,
    filter_nba_players,
    get_player_matches,
)

from .fixtures.api_responses import (
    empty_response,
    players_nba,
    players_non_nba,
)
from .fixtures.dataframes import expected_player_matches


class TestGetPlayerMatches:
    """test suite for get_player_matches"""

    @patch("rel_bball_analytics.players.player_info.get_data_from_api")
    def test_returns_dataframe_for_valid_matches(self, get_data_from_api, players_nba):
        get_data_from_api.return_value = players_nba
        results = get_player_matches(name="Curry")

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    @patch("rel_bball_analytics.players.player_info.get_data_from_api")
    def test_returns_none_if_no_matches(self, get_data_from_api, empty_response):
        get_data_from_api.return_value = empty_response
        results = get_player_matches(name="Fake")

        assert results is None

    @patch("rel_bball_analytics.players.player_info.get_data_from_api")
    def test_returns_none_if_no_nba_players(self, get_data_from_api, players_non_nba):
        get_data_from_api.return_value = players_non_nba
        results = get_player_matches(name="Wembanyama")

        assert results is None


class TestFilterNbaPlayers:
    """test suite for filter_nba_players"""

    def test_returns_nba_players(self, players_nba):
        players = pd.DataFrame(players_nba["response"])
        results = filter_nba_players(players=players)

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    def test_returns_empty_df_if_no_nba_players(self, players_non_nba):
        players = pd.DataFrame(players_non_nba["response"])
        results = filter_nba_players(players=players)

        assert type(results) == pd.DataFrame
        assert results.empty


class TestCleanPlayerData:
    """test suite for clean_player_data"""

    def test_returns_formatted_player_info(self, players_nba, expected_player_matches):
        players = pd.DataFrame(players_nba["response"])
        results = clean_player_data(players=players)

        assert results.equals(expected_player_matches)
