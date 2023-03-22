import pandas as pd

from rel_bball_analytics.api import get_data_from_api
from rel_bball_analytics.database import fetch_records, save_records

from .models import Player
from .utils import PLAYER_COLUMNS, calculate_age


def get_player_matches(name: str):
    """Return dataframe with general info on players that match the given search"""
    records = fetch_records(model=Player, lastname=name)

    if len(records) > 0:
        return pd.DataFrame(records)

    players = fetch_player_data(name=name)

    if players is None:
        return

    save_records(model=Player, items=players.to_dict(orient="records"))

    return players


def fetch_player_data(name: str):
    """Fetch results from API and return standardized player data"""
    player_data = get_data_from_api(endpoint="players", params={"name": name})

    if player_data["results"] == 0:
        return

    players = pd.DataFrame(player_data["response"])
    players = filter_nba_players(players=players)

    return clean_player_data(players=players) if not players.empty else None


def filter_nba_players(players: pd.DataFrame):
    """Return dataframe only containing players in the NBA"""
    players["is_nba"] = players["leagues"].apply(lambda obj: "standard" in obj.keys())
    return players.loc[players.is_nba]


def clean_player_data(players: pd.DataFrame):
    """Flatten nested JSON objects into valid rows in dataframe"""
    players["birth_date"] = players["birth"].apply(lambda obj: obj.get("date"))
    players["age"] = players["birth_date"].apply(calculate_age)
    players["country"] = players["birth"].apply(lambda obj: obj.get("country"))

    players["start_year"] = players["nba"].apply(lambda obj: obj.get("start"))
    players["pro_years"] = players["nba"].apply(lambda obj: obj.get("pro"))

    players["height_feet"] = players["height"].apply(lambda obj: obj.get("feets"))
    players["height_inches"] = players["height"].apply(lambda obj: obj.get("inches"))
    players["weight_pounds"] = players["weight"].apply(lambda obj: obj.get("pounds"))

    players["jersey"] = players["leagues"].apply(
        lambda obj: obj["standard"].get("jersey")
    )
    players["is_active"] = players["leagues"].apply(
        lambda obj: obj["standard"].get("active")
    )
    players["position"] = players["leagues"].apply(
        lambda obj: obj["standard"].get("pos")
    )

    return players[PLAYER_COLUMNS]
