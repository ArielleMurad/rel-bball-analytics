from datetime import datetime

from dateutil import relativedelta

PLAYER_COLUMNS = [
    "id",
    "firstname",
    "lastname",
    "birth_date",
    "age",
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

TABLE_COLUMNS = {
    "firstname": "First Name",
    "lastname": "Last Name",
    "age": "Age",
    "team": "Team",
    "position": "Position",
    "games_played": "GP",
    "points": "PPG",
    "field_goal_percentage": "FG%",
    "three_point_percentage": "3P%",
    "free_throw_percentage": "FT%",
    "total_rebounds": "TRB",
    "assists": "AST",
    "is_active": "Is Active?",
    "link": "",
}


def calculate_age(birth_date: str):
    """Calculate age from birth date string given in the api response"""
    if birth_date is None:
        return None

    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    delta = relativedelta.relativedelta(datetime.now(), birth_date)
    return delta.years
