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
    search_result["link"] = search_result.apply(
        lambda row: add_link(row["id"], int(row["season"])), axis=1
    )
    search_result["team"] = search_result["team"].apply(format_list)
    search_result["position"] = search_result["position"].apply(format_list)

    search_result = search_result.sort_values(by=["points"], ascending=False)
    search_result = search_result[TABLE_COLUMNS.keys()].rename(columns=TABLE_COLUMNS)

    return (
        search_result.style.format(precision=1, na_rep="")
        .set_table_styles(styles.players_table())
        .hide(axis=0)
        .to_html()
    )


def format_player_details(player_data: dict):
    """Format values according to design specifications"""
    player_data["season"] = format_season(int(player_data["season"]))
    player_data["team"] = format_list(player_data["team"])
    player_data["position"] = format_list(player_data["position"])

    for key, val in player_data.items():
        if isinstance(val, float):
            player_data[key] = round(val, 1)

        if val is None:
            player_data[key] = ""

    return player_data


def add_link(id, season):
    """Adds link to player details page"""
    return (
        f'<a href="{url_for("players.details", id=id, season=season)}">See Details</a>'
    )


def format_list(items: list):
    """Display array as comma separated list"""
    return ", ".join(items)


def format_season(season: int):
    """Display both years of the season"""
    return f"{season}-{season + 1}"
