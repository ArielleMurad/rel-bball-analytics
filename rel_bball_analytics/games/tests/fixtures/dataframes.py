from datetime import datetime

import pandas as pd
import pytest


@pytest.fixture()
def expected_clean_game_data():
    return pd.DataFrame(
        [
            {
                "id": 1,
                "season": 2022,
                "date": datetime(2022, 9, 30, 10),
                "home": "WAS",
                "away": "GSW",
                "home_score": 87,
                "away_score": 96,
                "winner": "GSW",
                "difference": 9,
            },
            {
                "id": 2,
                "season": 2022,
                "date": datetime(2022, 10, 2, 5),
                "home": "GSW",
                "away": "WAS",
                "home_score": 104,
                "away_score": 95,
                "winner": "GSW",
                "difference": 9,
            },
        ]
    )
