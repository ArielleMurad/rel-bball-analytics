from unittest.mock import patch

import pandas as pd

from rel_bball_analytics.database import db
from rel_bball_analytics.players.data_source import (
    clean_player_data,
    fetch_player_data,
    filter_nba_players,
    get_player_matches,
)

from .fixtures.api_responses import (
    empty_response,
    players_nba,
    players_non_nba,
)
from .fixtures.database import reset_test_db, setup_test_db
from .fixtures.db_records import player_record, players_valid
from .fixtures.expected import df_player_matches


class TestGetPlayerMatches:
    """test suite for get_player_matches"""

    @patch("rel_bball_analytics.players.data_source.fetch_player_data")
    def test_returns_existing_records_from_db(
        self, fetch_player_data, reset_test_db, player_record
    ):
        db.session.add(player_record)
        result = get_player_matches(name="Curry")

        assert type(result) == pd.DataFrame
        assert len(result) > 0
        assert not fetch_player_data.called

    @patch("rel_bball_analytics.players.data_source.save_records")
    @patch("rel_bball_analytics.players.data_source.fetch_player_data")
    def test_returns_data_from_api(
        self, fetch_player_data, save_records, reset_test_db, players_valid
    ):
        fetch_player_data.return_value = pd.DataFrame(players_valid)
        result = get_player_matches(name="Curry")

        assert type(result) == pd.DataFrame
        assert len(result) > 0
        assert fetch_player_data.called
        assert save_records.called

    @patch("rel_bball_analytics.players.data_source.fetch_player_data")
    def test_returns_none_if_no_matches_found(self, fetch_player_data):
        fetch_player_data.return_value = None
        result = get_player_matches(name="Curry")

        assert result is None
        assert fetch_player_data.called


class TestFetchPlayerData:
    """test suite for fetch_player_data"""

    @patch("rel_bball_analytics.players.data_source.get_data_from_api")
    def test_returns_dataframe_for_valid_matches(self, get_data_from_api, players_nba):
        get_data_from_api.return_value = players_nba
        results = fetch_player_data(name="Curry")

        assert type(results) == pd.DataFrame
        assert len(results) > 0

    @patch("rel_bball_analytics.players.data_source.get_data_from_api")
    def test_returns_none_if_no_matches(self, get_data_from_api, empty_response):
        get_data_from_api.return_value = empty_response
        results = fetch_player_data(name="Fake")

        assert results is None

    @patch("rel_bball_analytics.players.data_source.get_data_from_api")
    def test_returns_none_if_no_nba_players(self, get_data_from_api, players_non_nba):
        get_data_from_api.return_value = players_non_nba
        results = fetch_player_data(name="Wembanyama")

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

    def test_returns_formatted_player_info(self, players_nba, df_player_matches):
        players = pd.DataFrame(players_nba["response"])
        results = clean_player_data(players=players)

        assert results.equals(df_player_matches)
