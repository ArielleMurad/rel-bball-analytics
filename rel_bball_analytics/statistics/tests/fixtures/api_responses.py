import pytest


@pytest.fixture
def empty_response():
    return {
        "results": 0,
        "response": [],
    }


@pytest.fixture
def stats_full():
    return {
        "results": 2,
        "response": [
            {
                "player": {
                    "id": 124,
                },
                "team": {
                    "id": 11,
                    "code": "GSW",
                },
                "game": {"id": 1},
                "points": 16,
                "pos": "PG",
                "min": "16:30",
                "fgm": 7,
                "fga": 13,
                "fgp": "53.0",
                "ftm": 1,
                "fta": 1,
                "ftp": "100.0",
                "tpm": 2,
                "tpa": 8,
                "tpp": "25",
                "offReb": 0,
                "defReb": 5,
                "totReb": 5,
                "assists": 2,
                "pFouls": 1,
                "steals": 0,
                "turnovers": 5,
                "blocks": 1,
                "plusMinus": "-2",
                "comment": None,
            },
            {
                "player": {
                    "id": 124,
                },
                "team": {
                    "id": 11,
                    "code": "GSW",
                },
                "game": {"id": 2},
                "points": 34,
                "pos": "PG",
                "min": "38",
                "fgm": 13,
                "fga": 21,
                "fgp": "62.0",
                "ftm": 5,
                "fta": 5,
                "ftp": "100.0",
                "tpm": 4,
                "tpa": 8,
                "tpp": "50.0",
                "offReb": 0,
                "defReb": 7,
                "totReb": 7,
                "assists": 10,
                "pFouls": 1,
                "steals": 2,
                "turnovers": 3,
                "blocks": 0,
                "plusMinus": "+13",
                "comment": None,
            },
        ],
    }


@pytest.fixture
def stats_missing():
    return {
        "results": 1,
        "response": [
            {
                "player": {
                    "id": 121,
                },
                "team": {
                    "id": 11,
                    "code": "GSW",
                },
                "game": {"id": 1},
                "points": None,
                "pos": "PG",
                "min": None,
            },
        ],
    }
