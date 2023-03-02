import pytest

from rel_bball_analytics.players.models import Player


@pytest.fixture()
def players_valid():
    return [
        {
            "id": 124,
            "firstname": "Stephen",
            "lastname": "Curry",
            "season": 2022,
            "team_id": 11,
            "team": "GSW",
            "position": "PG",
        },
        {
            "id": 265,
            "firstname": "LeBron",
            "lastname": "James",
            "season": 2019,
            "team_id": 17,
            "team": "LAL",
            "position": "SF",
        },
    ]


@pytest.fixture()
def players_missing_required_field():
    return [
        {
            "id": 124,
            "firstname": "Stephen",
            "team_id": 11,
            "team": "GSW",
            "position": "PG",
        },
    ]


@pytest.fixture()
def players_duplicate():
    return [
        {
            "id": 124,
            "firstname": "Stephen",
            "lastname": "Curry",
            "season": 2022,
            "team_id": 11,
            "team": "GSW",
            "position": "PG",
        },
        {
            "id": 124,
            "firstname": "Stephen",
            "lastname": "Curry",
            "season": 2022,
            "team_id": 11,
            "team": "GSW",
            "position": "PG",
        },
    ]


@pytest.fixture()
def player_record():
    return Player(
        id=124,
        firstname="Stephen",
        lastname="Curry",
        season=2022,
        birth_date="1988-03-14",
        age=34,
        country="USA",
        height_feet=6,
        height_inches=2,
        weight_pounds=185,
        jersey=30,
        is_active=True,
        start_year=2009,
        pro_years=12,
        college="Davidson",
        team_id=11,
        team="GSW",
        position="PG",
        games_played=2,
        points=25,
        minutes_played=27.25,
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
