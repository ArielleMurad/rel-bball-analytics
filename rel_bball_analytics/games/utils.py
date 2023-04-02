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

GAME_LOG_COLUMNS = {
    "date": "Date",
    "team": "Team",
    "opponent": "Opp",
    "result": "Score",
    "position": "Pos",
    "minutes_played": "MP",
    "field_goals_made": "FG",
    "field_goal_attempts": "FGA",
    "field_goal_percentage": "FG%",
    "three_points_made": "3P",
    "three_point_attempts": "3PA",
    "three_point_percentage": "3P%",
    "free_throws_made": "FT",
    "free_throw_attempts": "FTA",
    "free_throw_percentage": "FT%",
    "offensive_rebounds": "ORB",
    "defensive_rebounds": "DRB",
    "total_rebounds": "TRB",
    "assists": "AST",
    "steals": "STL",
    "blocks": "BLK",
    "turnovers": "TOV",
    "personal_fouls": "PF",
    "points": "PTS",
}


def get_winner(row):
    return row["home"] if row["home_score"] > row["away_score"] else row["away"]


def parse_date(date):
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.000Z")
