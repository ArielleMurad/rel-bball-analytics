import pandas as pd
import pytest


@pytest.fixture()
def expected_clean_stats_data():
    return pd.DataFrame(
        [
            {
                "game_id": 1,
                "team_id": 11,
                "team": "GSW",
                "position": "PG",
                "points": 16,
                "minutes_played": 16.5,
                "field_goals_made": 7,
                "field_goal_attempts": 13,
                "field_goal_percentage": 53.0,
                "three_points_made": 2,
                "three_point_attempts": 8,
                "three_point_percentage": 25,
                "free_throws_made": 1,
                "free_throw_attempts": 1,
                "free_throw_percentage": 100.0,
                "offensive_rebounds": 0,
                "defensive_rebounds": 5,
                "total_rebounds": 5,
                "assists": 2,
                "steals": 0,
                "blocks": 1,
                "turnovers": 5,
                "personal_fouls": 1,
            },
            {
                "game_id": 2,
                "team_id": 11,
                "team": "GSW",
                "position": "PG",
                "points": 34,
                "minutes_played": 38,
                "field_goals_made": 13,
                "field_goal_attempts": 21,
                "field_goal_percentage": 62.0,
                "three_points_made": 4,
                "three_point_attempts": 8,
                "three_point_percentage": 50.0,
                "free_throws_made": 5,
                "free_throw_attempts": 5,
                "free_throw_percentage": 100.0,
                "offensive_rebounds": 0,
                "defensive_rebounds": 7,
                "total_rebounds": 7,
                "assists": 10,
                "steals": 2,
                "blocks": 0,
                "turnovers": 3,
                "personal_fouls": 1,
            },
        ]
    )


@pytest.fixture()
def expected_player_stats(expected_clean_stats_data):
    player_stats = expected_clean_stats_data
    player_stats["player_id"] = 124
    player_stats["season"] = 2022

    return player_stats


@pytest.fixture()
def expected_player_summary_stats():
    return {
        "id": 124,
        "season": 2022,
        "team": ["GSW"],
        "position": ["PG"],
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
