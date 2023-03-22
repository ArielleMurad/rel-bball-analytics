STATS_COLUMNS = {
    "game_id": "game_id",
    "team_id": "team_id",
    "team_code": "team",
    "pos": "position",
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


def time_to_int(time: str):
    """Convert time strings from api response to int"""
    if time is None:
        return time

    if ":" in time:
        mins, secs = time.split(":")
        result = int(mins) + int(secs) / 60
    else:
        result = int(time)

    return round(result, 2)
