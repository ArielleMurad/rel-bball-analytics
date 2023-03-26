from datetime import datetime

GAME_COLUMNS = [
    "id",
    "season",
    "date",
    "home",
    "away",
    "home_score",
    "away_score",
    "winner",
    "difference",
]


def get_winner(row):
    return row["home"] if row["home_score"] > row["away_score"] else row["away"]


def parse_date(date):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.000Z")
