import pandas as pd
import pytest


@pytest.fixture()
def expected_player_matches():
    return pd.DataFrame(
        [
            {
                "id": 124,
                "firstname": "Stephen",
                "lastname": "Curry",
                "birth_date": "1988-03-14",
                "country": "USA",
                "height_feet": "6",
                "height_inches": "2",
                "weight_pounds": "185",
                "jersey": 30,
                "is_active": True,
                "start_year": 2009,
                "pro_years": 12,
                "college": "Davidson",
            }
        ]
    )


@pytest.fixture()
def expected_clean_stats_data():
    return pd.DataFrame(
        [
            {
                "points": 16,
                "pos": "PG",
                "min": 16.5,
                "fgm": 7,
                "fga": 13,
                "fgp": 53.0,
                "ftm": 1,
                "fta": 1,
                "ftp": 100.0,
                "tpm": 2,
                "tpa": 8,
                "tpp": 25,
                "offReb": 0,
                "defReb": 5,
                "totReb": 5,
                "assists": 2,
                "pFouls": 1,
                "steals": 0,
                "turnovers": 5,
                "blocks": 1,
                "player_id": 124,
                "team_id": 11,
                "team_code": "GSW",
                "game_id": 1,
            },
            {
                "points": 34,
                "pos": "PG",
                "min": 38,
                "fgm": 13,
                "fga": 21,
                "fgp": 62.0,
                "ftm": 5,
                "fta": 5,
                "ftp": 100.0,
                "tpm": 4,
                "tpa": 8,
                "tpp": 50.0,
                "offReb": 0,
                "defReb": 7,
                "totReb": 7,
                "assists": 10,
                "pFouls": 1,
                "steals": 2,
                "turnovers": 3,
                "blocks": 0,
                "player_id": 124,
                "team_id": 11,
                "team_code": "GSW",
                "game_id": 2,
            },
        ]
    )


@pytest.fixture()
def expected_player_summary_stats():
    return {
        "id": 124,
        "season": 2022,
        "team_id": 11,
        "team": "GSW",
        "position": "PG",
        "games_played": 2,
        "points": 25,
        "minutes_played": 27.25,
        "field_goals_made": 10,
        "field_goal_attempts": 17,
        "field_goal_percentage": 57.5,
        "three_points_made": 3,
        "three_point_attempts": 8,
        "three_point_percentage": 37.5,
        "free_throws_made": 3,
        "free_throw_attempts": 3,
        "free_throw_percentage": 100,
        "offensive_rebounds": 0,
        "defensive_rebounds": 6,
        "total_rebounds": 6,
        "assists": 6,
        "steals": 1,
        "blocks": 0.5,
        "turnovers": 4,
        "personal_fouls": 1,
    }
