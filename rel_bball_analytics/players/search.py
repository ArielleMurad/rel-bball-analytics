import logging

import pandas as pd

from .models import fetch_player_records, save_player_records
from .player_info import get_player_matches
from .summary_stats import get_summary_stats

logger = logging.getLogger(__name__)


def get_search_result(name: str, season: int):
    """Query db for exisiting records, if no matches found then make API request"""
    records = fetch_player_records(lastname=name, season=season)

    if len(records) > 0:
        return pd.DataFrame(records)

    return fetch_from_api(name=name, season=season)


def fetch_from_api(name: str, season: int):
    """Return info and summary stats for each player from the API"""
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

    results["id"] = results.apply(lambda row: f"{row['id']}_{row['season']}", axis=1)
    save_player_records(players=results.to_dict(orient="records"))

    return results
