from datetime import datetime

import requests
from dateutil import relativedelta

from rel_bball_analytics import app


def get_data_from_api(endpoint: str, params: dict):
    """Return JSON response from GET request to nba.api-sports.io"""
    url = app.config["SPORTS_API_URL"] + endpoint
    headers = {"x-rapidapi-key": app.config["SPORTS_API_KEY"]}

    response = requests.get(url, params=params, headers=headers)
    return response.json()


def time_to_int(time: str):
    """Convert time strings from api response to int"""
    if time is None:
        return time

    if ":" in time:
        mins, secs = time.split(":")
        result = int(mins) + int(secs) / 60
    else:
        result = int(time)

    return round(result, 2)


def calculate_age(birth_date: str):
    """Calculate age from birth date string given in the api response"""
    if birth_date is None:
        return None

    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    delta = relativedelta.relativedelta(datetime.now(), birth_date)
    return delta.years
