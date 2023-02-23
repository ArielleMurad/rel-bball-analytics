import pandas as pd

from .utils import get_data_from_api, time_to_int

STATS_COLUMNS = {
    "points": "points",
    "min": "minutes_played",
    "fgm": "field_goals_made",
    "fga": "field_goal_attempts",
    "fgp": "field_goal_percentage",
    "tpm": "three_points_made",
    "tpa": "three_point_attempts",
    "tpp": "three_point_percentage",
    "ftm": "free_throws_made",
    "fta": "free_throw_attempts",
    "ftp": "free_throw_percentage",
    "offReb": "offensive_rebounds",
    "defReb": "defensive_rebounds",
    "totReb": "total_rebounds",
    "assists": "assists",
    "steals": "steals",
    "blocks": "blocks",
    "turnovers": "turnovers",
    "pFouls": "personal_fouls",
}

EXCLUDED_STATS_COLUMNS = [
    "player",
    "team",
    "game",
    "comment",
    "plusMinus",
]


def get_summary_stats(player_ids: list, season: int):
    """Return dataframe with summary stats for each player"""
    summary_stats = []
    for id in player_ids:
        params = {"id": id, "season": season}
        stats_data = get_data_from_api(endpoint="players/statistics", params=params)

        if stats_data["results"] == 0:
            continue

        stats = pd.DataFrame(stats_data["response"])
        stats = clean_stats_data(stats=stats)

        if stats is None:
            continue

        player_summary_stats = get_player_summary_stats(
            id=id, season=season, stats=stats
        )
        summary_stats.append(player_summary_stats)

    return pd.DataFrame(summary_stats)


def clean_stats_data(stats: pd.DataFrame):
    """Flatten nested JSON object into valid row in dataframe and drop null values"""
    stats = stats.dropna(subset=["points", "min"])

    if stats.empty:
        return

    stats["team_id"] = stats["team"].apply(lambda obj: obj["id"])
    stats["team_code"] = stats["team"].apply(lambda obj: obj["code"])
    stats["game_id"] = stats["game"].apply(lambda obj: obj["id"])
    stats["min"] = stats["min"].apply(time_to_int)

    for col in ["fgp", "ftp", "tpp"]:
        stats[col] = stats[col].astype(float)

    return stats.drop(EXCLUDED_STATS_COLUMNS, axis=1)


def get_player_summary_stats(id: int, season: int, stats: pd.DataFrame):
    """Return obj with summary stats for given id and season"""
    stats_data = stats[STATS_COLUMNS.keys()].rename(columns=STATS_COLUMNS)
    summary_stats = stats_data.mean(axis=0, numeric_only=True)

    return {
        "id": id,
        "season": season,
        "team_id": stats["team_id"].mode()[0],
        "team": stats["team_code"].mode()[0],
        "position": stats["pos"].mode()[0],
        "games_played": len(stats),
        **summary_stats,
    }
