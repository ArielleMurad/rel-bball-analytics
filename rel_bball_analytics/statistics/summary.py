import pandas as pd

from .data_source import get_player_stats

EXCLUDED_COLUMNS = [
    "player_id",
    "team_id",
    "game_id",
]


def get_summary_stats(player_ids: list, season: int):
    """Return dataframe with summary stats for each player"""
    summary_stats = []
    for player_id in player_ids:
        player_stats = get_player_stats(player_id=player_id, season=season)

        if player_stats is None:
            continue

        player_summary_stats = get_player_summary_stats(stats=player_stats)
        summary_stats.append(player_summary_stats)

    return pd.DataFrame(summary_stats)


def get_player_summary_stats(stats: pd.DataFrame):
    """Return obj with summary stats for given id and season"""
    summary_stats = (
        stats.drop(EXCLUDED_COLUMNS, axis=1).mean(axis=0, numeric_only=True).to_dict()
    )

    return {
        "id": stats["player_id"].iloc[0],
        "season": stats["season"].iloc[0],
        "team": stats["team"].dropna().unique(),
        "position": stats["position"].dropna().unique(),
        "games_played": len(stats),
        **summary_stats,
    }
