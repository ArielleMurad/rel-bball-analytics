import pytest


@pytest.fixture
def empty_response():
    return {
        "results": 0,
        "response": [],
    }


@pytest.fixture
def players_nba():
    return {
        "results": 1,
        "response": [
            {
                "id": 124,
                "firstname": "Stephen",
                "lastname": "Curry",
                "birth": {"date": "1988-03-14", "country": "USA"},
                "nba": {"start": 2009, "pro": 12},
                "height": {
                    "feets": "6",
                    "inches": "2",
                },
                "weight": {
                    "pounds": "185",
                },
                "college": "Davidson",
                "leagues": {
                    "standard": {
                        "jersey": 30,
                        "active": True,
                    }
                },
            }
        ],
    }


@pytest.fixture
def players_non_nba():
    return {
        "results": 1,
        "response": [
            {
                "id": 122,
                "firstname": "Victor",
                "lastname": "Wembanyama",
                "leagues": {
                    "france": {
                        "jersey": 32,
                        "active": True,
                    }
                },
            }
        ],
    }
