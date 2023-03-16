import pytest

from rel_bball_analytics.players.models import Player


@pytest.fixture()
def players_valid():
    return [
        {
            "id": 124,
            "firstname": "Stephen",
            "lastname": "Curry",
            "birth_date": "1988-03-14",
            "age": 35,
            "country": "USA",
            "jersey": 30,
            "is_active": True,
        },
        {
            "id": 265,
            "firstname": "LeBron",
            "lastname": "James",
            "birth_date": "1988-03-14",
            "age": 38,
            "country": "USA",
            "jersey": 6,
            "is_active": True,
        },
    ]


@pytest.fixture()
def players_missing_required_field():
    return [
        {
            "id": 124,
            "birth_date": "1988-03-14",
            "age": 35,
            "country": "USA",
            "jersey": 30,
            "is_active": True,
        },
    ]


@pytest.fixture()
def players_duplicate():
    return [
        {
            "id": 124,
            "firstname": "Stephen",
            "lastname": "Curry",
            "birth_date": "1988-03-14",
            "age": 35,
            "country": "USA",
            "jersey": 30,
            "is_active": True,
        },
        {
            "id": 124,
            "firstname": "Stephen",
            "lastname": "Curry",
            "birth_date": "1988-03-14",
            "age": 35,
            "country": "USA",
            "jersey": 30,
            "is_active": True,
        },
    ]


@pytest.fixture()
def player_record():
    return Player(
        id=124,
        firstname="Stephen",
        lastname="Curry",
        birth_date="1988-03-14",
        age=35,
        country="USA",
        height_feet=6,
        height_inches=2,
        weight_pounds=185,
        jersey=30,
        is_active=True,
        start_year=2009,
        pro_years=12,
        college="Davidson",
    )
