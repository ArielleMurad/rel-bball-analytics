from datetime import datetime

from dateutil import relativedelta


def calculate_age(birth_date: str):
    """Calculate age from birth date string given in the api response"""
    if birth_date is None:
        return None

    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    delta = relativedelta.relativedelta(datetime.now(), birth_date)
    return delta.years
