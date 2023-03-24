import pandas as pd

from rel_bball_analytics.database import fetch_records
from rel_bball_analytics.statistics.models import Statistic

from .data_source import get_game_stats


def get_game_log(player_id: int, season: int):
    player_stats = fetch_records(model=Statistic, player_id=player_id, season=season)
    player_stats = pd.DataFrame(player_stats)

    team_ids = player_stats["team_id"].unique()
    teams = player_stats["team"].unique()

    game_stats = pd.DataFrame()
    for index in range(len(team_ids)):
        team_game_stats = get_game_stats(
            team_id=team_ids[index], team=teams[index], season=season
        )

        if team_game_stats is None:
            continue

        game_stats = game_stats.append(team_game_stats)

    return player_stats.merge(game_stats, left_on="game_id", right_on="id")
