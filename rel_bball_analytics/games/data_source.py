import pandas as pd

from rel_bball_analytics.api import get_data_from_api
from rel_bball_analytics.database import delete_records, save_records

from .models import Game
from .utils import GAME_COLUMNS, get_winner, parse_date


def get_game_stats(team_id: int, team: str, season: int):
    """Return dataframe with games played by given team in season"""
    games = fetch_game_data(team_id=team_id, season=season)

    if games is None:
        return

    # Update existing records if any
    or_clause = {"home": team, "away": team}
    delete_records(model=Game, or_clause=or_clause, season=season)
    save_records(model=Game, items=games.to_dict(orient="records"))

    return games


def fetch_game_data(team_id: int, season: int):
    """Fetch results from API and return standardized game data"""
    params = {"team": team_id, "season": season, "league": "Standard"}
    game_data = get_data_from_api(endpoint="games", params=params)

    if game_data["results"] == 0:
        return

    games = pd.DataFrame(game_data["response"])
    games = filter_finished_games(games=games)

    return clean_game_data(games=games) if not games.empty else None


def filter_finished_games(games: pd.DataFrame):
    """Return dataframe only containing finished games"""
    games["is_finished"] = games["status"].apply(lambda obj: obj["long"] == "Finished")
    return games.loc[games.is_finished]


def clean_game_data(games: pd.DataFrame):
    """Flatten nested JSON object into valid rows in dataframe"""
    games["date"] = games["date"].apply(lambda obj: parse_date(obj.get("start")))
    games["home"] = games["teams"].apply(lambda obj: obj["home"].get("code"))
    games["away"] = games["teams"].apply(lambda obj: obj["visitors"].get("code"))
    games["home_score"] = games["scores"].apply(lambda obj: obj["home"].get("points"))
    games["away_score"] = games["scores"].apply(
        lambda obj: obj["visitors"].get("points")
    )
    games["difference"] = abs(games["home_score"] - games["away_score"])
    games["winner"] = games.apply(get_winner, axis=1)

    return games[GAME_COLUMNS]
