import pandas as pd
import pytest


@pytest.fixture()
def df_player_matches():
    return pd.DataFrame(
        [
            {
                "id": 124,
                "firstname": "Stephen",
                "lastname": "Curry",
                "birth_date": "1988-03-14",
                "age": 35,
                "country": "USA",
                "height_feet": "6",
                "height_inches": "2",
                "weight_pounds": "185",
                "jersey": 30,
                "is_active": True,
                "start_year": 2009,
                "pro_years": 12,
                "college": "Davidson",
            }
        ]
    )
