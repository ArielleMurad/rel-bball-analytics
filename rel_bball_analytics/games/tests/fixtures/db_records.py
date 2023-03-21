from datetime import datetime

import pytest

from rel_bball_analytics.games.models import Game


@pytest.fixture()
def games_valid():
    return [
        {
            "id": 1,
            "season": 2022,
            "date": datetime.now(),
            "home": "GSW",
            "away": "WAS",
            "home_score": 104,
            "away_score": 95,
            "winner": "GSW",
            "difference": 9,
        },
        {
            "id": 2,
            "season": 2022,
            "date": datetime.now(),
            "home": "DEN",
            "away": "GSW",
            "home_score": 119,
            "away_score": 112,
            "winner": "DEN",
            "difference": 7,
        },
    ]


@pytest.fixture()
def games_missing_required_field():
    return [
        {
            "id": 1,
            "home": "GSW",
            "away": "WAS",
            "home_score": 104,
            "away_score": 95,
        },
    ]


@pytest.fixture()
def games_duplicate():
    return [
        {
            "id": 1,
            "season": 2022,
            "date": datetime.now(),
            "home": "GSW",
            "away": "WAS",
            "home_score": 104,
            "away_score": 95,
            "winner": "GSW",
            "difference": 9,
        },
        {
            "id": 1,
            "season": 2022,
            "date": datetime.now(),
            "home": "GSW",
            "away": "WAS",
            "home_score": 104,
            "away_score": 95,
            "winner": "GSW",
            "difference": 9,
        },
    ]


@pytest.fixture()
def game_record():
    return Game(
        id="124_10101",
        season=2022,
        date=datetime.now(),
        home="GSW",
        away="WAS",
        home_score=104,
        away_score=95,
        winner="GSW",
        difference=9,
    )
