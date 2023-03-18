import requests

from rel_bball_analytics import app


def get_data_from_api(endpoint: str, params: dict):
    """Return JSON response from GET request to nba.api-sports.io"""
    url = app.config["SPORTS_API_URL"] + endpoint
    headers = {"x-rapidapi-key": app.config["SPORTS_API_KEY"]}

    response = requests.get(url, params=params, headers=headers)
    return response.json()
