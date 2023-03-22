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


def calculate_age(birth_date: str):
    """Calculate age from birth date string given in the api response"""
    if birth_date is None:
        return None

    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    delta = relativedelta.relativedelta(datetime.now(), birth_date)
    return delta.years
