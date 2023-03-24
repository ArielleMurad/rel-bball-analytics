from unittest.mock import patch

from rel_bball_analytics.database import db
from rel_bball_analytics.games.game_log import get_game_log
from rel_bball_analytics.statistics.tests.fixtures.db_records import stats_record

from .fixtures.database import reset_test_db, setup_test_db
from .fixtures.expected import df_game_data


class TestGetGameLog:
    """test suite for get_game_log"""

    @patch("rel_bball_analytics.games.game_log.get_game_stats")
    def test_returns_game_log_for_player(
        self, get_game_stats, reset_test_db, stats_record, df_game_data
    ):
        db.session.add(stats_record)
        get_game_stats.return_value = df_game_data
        results = get_game_log(player_id=124, season=2022)

        assert results.iloc[0]["game_id"] == 1
        assert results.iloc[0]["team"] == "GSW"
        assert results.iloc[0]["points"] == 25
        assert results.iloc[0]["winner"] == "GSW"
        assert results.iloc[0]["difference"] == 9
