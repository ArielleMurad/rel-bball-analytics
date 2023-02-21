import pandas as pd

from .utils import get_data_from_api

PLAYER_COLUMNS = [
    "id",
    "firstname",
    "lastname",
    "birth_date",
    "country",
    "height_feet",
    "height_inches",
    "weight_pounds",
    "jersey",
    "is_active",
    "start_year",
    "pro_years",
    "college",
]


def get_player_matches(name: str):
    """Return dataframe with general info on players that match the given search"""
    player_data = get_data_from_api(endpoint="players", params={"name": name})

    if player_data["results"] == 0:
        return

    players = pd.DataFrame(player_data["response"])
    players = filter_nba_players(players=players)
    return clean_player_data(players=players)


def filter_nba_players(players: pd.DataFrame):
    """Return dataframe only containing players in the NBA"""
    players["is_nba"] = players["leagues"].apply(lambda obj: "standard" in obj.keys())
    return players.loc[players.is_nba]


def clean_player_data(players: pd.DataFrame):
    """Flatten nested JSON object into valid row in dataframe"""
    players["birth_date"] = players["birth"].apply(lambda obj: obj.get("date"))
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
