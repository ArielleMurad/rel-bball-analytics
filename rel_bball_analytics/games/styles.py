import pandas as pd

import rel_bball_analytics.static.py.games as styles

from .utils import GAME_LOG_COLUMNS


def format_game_log(game_log: pd.DataFrame):
    """Returns HTML with formatted game log table to be displayed on details page"""
    game_log = game_log.sort_values(by=["date"])

    game_log["date"] = game_log["date"].apply(format_date)
    game_log["result"] = game_log.apply(format_result, axis=1)
    game_log["opponent"] = game_log.apply(get_opponent, axis=1)

    game_log = game_log[GAME_LOG_COLUMNS.keys()].rename(columns=GAME_LOG_COLUMNS)

    return (
        game_log.style.format(precision=1, na_rep="")
        .set_table_styles(styles.game_log_table())
        .hide(axis=0)
        .to_html()
    )


def format_date(date):
    return date.date().strftime("%Y-%m-%d")


def format_result(row):
    result = "W" if row["team"] == row["winner"] else "L"
    sign = "+" if row["team"] == row["winner"] else "-"

    return f"{result} ({sign}{row['difference']})"


def get_opponent(row):
    return row["home"] if row["team"] == row["away"] else row["away"]
