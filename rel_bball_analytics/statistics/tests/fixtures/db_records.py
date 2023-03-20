import pytest

from rel_bball_analytics.statistics.models import Statistic


@pytest.fixture()
def stats_valid():
    return [
        {
            "id": "124_10101",
            "player_id": 124,
            "game_id": 10101,
            "season": 2022,
            "team_id": 11,
            "team": "GSW",
            "position": "PG",
        },
        {
            "id": "265_20202",
            "player_id": 256,
            "game_id": 20202,
            "season": 2019,
            "team_id": 17,
            "team": "LAL",
            "position": "SF",
        },
    ]


@pytest.fixture()
def stats_missing_required_field():
    return [
        {
            "id": "124_10101",
            "player_id": 124,
            "game_id": 10101,
        },
    ]


@pytest.fixture()
def stats_duplicate():
    return [
        {
            "id": "124_10101",
            "player_id": 124,
            "game_id": 10101,
            "season": 2022,
            "team_id": 11,
            "team": "GSW",
            "position": "PG",
        },
        {
            "id": "124_10101",
            "player_id": 124,
            "game_id": 10101,
            "season": 2022,
            "team_id": 11,
            "team": "GSW",
            "position": "PG",
        },
    ]


@pytest.fixture()
def stats_record():
    return Statistic(
        id="124_10101",
        player_id=124,
        game_id=10101,
        season=2022,
        team_id=11,
        team="GSW",
        position="PG",
        points=25,
        minutes_played=27,
        field_goals_made=10,
        field_goal_attempts=17,
        field_goal_percentage=57.5,
        three_points_made=3,
        three_point_attempts=8,
        three_point_percentage=37.5,
        free_throws_made=3,
        free_throw_attempts=3,
        free_throw_percentage=100,
        offensive_rebounds=0,
        defensive_rebounds=6,
        total_rebounds=6,
        assists=6,
        steals=1,
        blocks=0.5,
        turnovers=4,
        personal_fouls=1,
    )
