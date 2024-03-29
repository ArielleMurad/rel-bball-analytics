import pandas as pd

from rel_bball_analytics.api import get_data_from_api
from rel_bball_analytics.database import delete_records, save_records

from .models import Statistic
from .utils import STATS_COLUMNS, time_to_int


def get_player_stats(player_id: int, season: int):
    """Return dataframe with given player's stats for each game in season"""
    stats = fetch_stats_data(player_id=player_id, season=season)

    if stats is None:
        return

    stats["id"] = stats["game_id"].apply(lambda game_id: f"{player_id}_{game_id}")
    stats["player_id"] = player_id
    stats["season"] = season

    # Update existing records if any
    delete_records(model=Statistic, player_id=player_id, season=season)
    save_records(model=Statistic, items=stats.to_dict(orient="records"))

    return stats


def fetch_stats_data(player_id: int, season: int):
    """Fetch results from API and return standardized stats data"""
    params = {"id": player_id, "season": season}
    stats_data = get_data_from_api(endpoint="players/statistics", params=params)

    if stats_data["results"] == 0:
        return

    stats = pd.DataFrame(stats_data["response"])
    return clean_stats_data(stats=stats)


def clean_stats_data(stats: pd.DataFrame):
    """Flatten nested JSON object into valid row in dataframe and drop null values"""
    stats.dropna(subset=["points", "min"], inplace=True)

    if stats.empty:
        return

    stats["team_id"] = stats["team"].apply(lambda obj: obj["id"])
    stats["team_code"] = stats["team"].apply(lambda obj: obj["code"])
    stats["game_id"] = stats["game"].apply(lambda obj: obj["id"])
    stats["min"] = stats["min"].apply(time_to_int)

    for col in ["fgp", "ftp", "tpp"]:
        stats[col] = stats[col].astype(float)

    return stats[STATS_COLUMNS.keys()].rename(columns=STATS_COLUMNS)
