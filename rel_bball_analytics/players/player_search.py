import pandas as pd

import rel_bball_analytics.static.styles.players as styles
from rel_bball_analytics import app

from .player_info import get_player_matches
from .summary_stats import get_summary_stats

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


def player_search(name: str, season: int):
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
