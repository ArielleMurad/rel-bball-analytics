import pandas as pd
from flask import url_for

import rel_bball_analytics.static.py.players as styles

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
    "link": "",
}


def format_search_result(search_result: pd.DataFrame):
    """Returns HTML with formatted players table to be displayed on search page"""
    search_result["is_active"] = search_result["is_active"].apply(
        lambda val: "Yes" if val is True else "No"
    )
    search_result["link"] = search_result.apply(lambda row: add_link(row["id"]), axis=1)

    search_result = search_result.sort_values(by=["points"], ascending=False)
    search_result = search_result[TABLE_COLUMNS.keys()].rename(columns=TABLE_COLUMNS)

    return (
        search_result.style.format(precision=1, na_rep="")
        .set_table_styles(styles.players_table())
        .hide(axis=0)
        .to_html()
    )


def add_link(id):
    """Adds link to player details page"""
    return f'<a href="{url_for("players.details", id=id)}">See Details</a>'


def round_stats(stats: dict, precision=1):
    """Rounds statsitics to amount of decimal places specified by precision"""
    return {
        key: round(val, precision) if type(val) is float else val
        for key, val in stats.items()
    }
