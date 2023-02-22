import requests

from rel_bball_analytics import app

CURRENT_SEASON = 2022


def get_data_from_api(endpoint: str, params: dict):
    """Return JSON response from GET request to nba.api-sports.io"""
    url = app.config["SPORTS_API_URL"] + endpoint
    headers = {"x-rapidapi-key": app.config["SPORTS_API_KEY"]}

    response = requests.get(url, params=params, headers=headers)
    return response.json()


def time_to_int(time):
    if time is None:
        return time

    if ":" in time:
        mins, secs = time.split(":")
        result = int(mins) + int(secs) / 60
        return round(result, 2)

    return round(int(time), 2)
