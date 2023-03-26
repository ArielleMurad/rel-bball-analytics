import logging

import pandas as pd

from rel_bball_analytics.database import fetch_records
from rel_bball_analytics.statistics.models import Statistic
from rel_bball_analytics.statistics.summary import (
    get_player_summary_stats,
    get_summary_stats,
)

from .data_source import get_player_matches
from .models import Player

logger = logging.getLogger(__name__)


def get_search_result(name: str, season: int):
    """Return info and summary stats for each player"""
    players = get_player_matches(name=name)

    if players is None:
        logger.info(f"No matches found for '{name}' in the {season} season")
        return

    player_ids = players["id"].unique()
    summary_stats = get_summary_stats(player_ids=player_ids, season=season)

    if summary_stats.empty:
        logger.info(f"No statistics available for '{name}' in the {season} season")
        return

    results = players.merge(summary_stats, how="inner", on="id")
    logger.info(f"{len(results)} results found for '{name}' in the {season} season")

    return results


def get_player_details(id: int, season: int):
    """Return player details including summary stats for given player in season"""
    player = fetch_records(model=Player, id=id)[0]

    stats = fetch_records(model=Statistic, player_id=id, season=season)
    summary_stats = get_player_summary_stats(stats=pd.DataFrame(stats))

    return {**player, **summary_stats}
