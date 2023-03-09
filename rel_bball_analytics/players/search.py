import logging

import pandas as pd

import rel_bball_analytics.static.styles.players as styles

from .models import fetch_player_records, save_player_records
from .player_info import get_player_matches
from .summary_stats import get_summary_stats

logger = logging.getLogger(__name__)

TABLE_COLUMNS = {
    "firstname": "First Name",
    "lastname": "Last Name",
    "age": "Age",
    "team": "Team",
    "position": "Position",
    "games_played": "GP",
    "points": "PPG",
    "field_goal_percentage": "FG%",
    "three_point_percentage": "FG3%",
    "free_throw_percentage": "FT%",
    "total_rebounds": "TRB",
    "assists": "AST",
    "is_active": "Is Active?",
}


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


def format_search_result(search_result: pd.DataFrame):
    """Returns HTML with formatted players table to be displayed on search page"""
    search_result["is_active"] = search_result["is_active"].apply(
        lambda val: "Yes" if val is True else "No"
    )

    search_result = search_result.sort_values(by=["points"], ascending=False)
    search_result = search_result[TABLE_COLUMNS.keys()].rename(columns=TABLE_COLUMNS)

    return (
        search_result.style.format(precision=1, na_rep="")
        .set_table_styles(styles.players_table())
        .hide(axis=0)
        .to_html()
    )
