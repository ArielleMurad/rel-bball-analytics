import pytest


@pytest.fixture
def empty_response():
    return {
        "results": 0,
        "response": [],
    }


@pytest.fixture
def games_finished():
    return {
        "results": 2,
        "response": [
            {
                "id": 1,
                "league": "standard",
                "season": 2022,
                "date": {
                    "start": "2022-09-30T10:00:00.000Z",
                    "end": "2022-09-30T12:34:00.000Z",
                    "duration": "2:18",
                },
                "status": {"short": 3, "long": "Finished"},
                "teams": {
                    "visitors": {
                        "id": 11,
                        "code": "GSW",
                    },
                    "home": {
                        "id": 41,
                        "code": "WAS",
                    },
                },
                "scores": {
                    "visitors": {"linescore": ["16", "25", "28", "27"], "points": 96},
                    "home": {"linescore": ["12", "25", "27", "23"], "points": 87},
                },
            },
            {
                "id": 2,
                "league": "standard",
                "season": 2022,
                "date": {
                    "start": "2022-10-02T05:00:00.000Z",
                    "end": "2022-10-02T07:28:00.000Z",
                    "duration": "2:14",
                },
                "status": {"short": 3, "long": "Finished"},
                "teams": {
                    "visitors": {
                        "id": 41,
                        "code": "WAS",
                    },
                    "home": {
                        "id": 11,
                        "code": "GSW",
                    },
                },
                "scores": {
                    "visitors": {"linescore": ["25", "31", "29", "10"], "points": 95},
                    "home": {"linescore": ["26", "28", "20", "30"], "points": 104},
                },
            },
        ],
    }


@pytest.fixture
def games_unfinished():
    return {
        "results": 1,
        "response": [
            {
                "id": 0,
                "league": "standard",
                "season": 2022,
                "date": {
                    "start": "2023-03-25T02:00:00.000Z",
                    "end": None,
                    "duration": None,
                },
                "status": {"short": 1, "long": "Scheduled"},
                "teams": {
                    "visitors": {
                        "id": 27,
                        "code": "PHI",
                    },
                    "home": {
                        "id": 11,
                        "code": "GSW",
                    },
                },
                "scores": {
                    "visitors": {"linescore": [], "points": None},
                    "home": {"linescore": [], "points": None},
                },
            },
        ],
    }
