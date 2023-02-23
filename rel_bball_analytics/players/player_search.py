import pandas as pd

from rel_bball_analytics import app

from .player_info import get_player_matches
from .summary_stats import get_summary_stats
from .utils import CURRENT_SEASON


def player_search(name: str, season=CURRENT_SEASON):
    """Return info and summary stats for each player matching given search"""
    players = get_player_matches(name=name)

    if players is None:
        app.logger.info(f"No matches found for '{name}' in the {season} season")
        return

    player_ids = players["id"].unique()
    summary_stats = get_summary_stats(player_ids=player_ids, season=season)

    if summary_stats.empty:
        app.logger.info(f"No statistics available for '{name}' in the {season} season")
        return

    results = players.merge(summary_stats, how="inner", on="id")
    app.logger.info(f"{len(results)} results found for '{name}' in the {season} season")

    return results
