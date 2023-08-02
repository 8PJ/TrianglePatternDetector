from detection.detection_functionality.highs_lows import mark_highs_lows

import pandas as pd
import pytest

@pytest.fixture
def high_low_data():
    data = {
        "open": [
            0, 0, 0, 0, 0, 0, 0,
        ],
        "close": [
            0, 0, 0, 0, 0, 0, 0,
        ],
        "high": [
            1, 1, 1, 1, 1, 1, 1,
        ],
        "low": [
            1, 1, 1, 1, 1, 1, 1,
        ],
        "volume": [
            1, 1, 1, 1, 1, 1, 1,
        ],
        "number_transactions": [
            1, 1, 1, 1, 1, 1, 1,
        ],
        "time": [
            "2023-08-02 07:00:00",
            "2023-08-02 08:00:00",
            "2023-08-02 08:00:00",
            "2023-08-02 08:00:00",
            "2023-08-02 08:00:00",
            "2023-08-02 08:00:00",
            "2023-08-02 08:00:00",
        ],
    }

    return data


def test_marks_high_point(high_low_data):
    high_low_data["high"] = [1, 2, 3, 4, 3, 2, 1]

    df = pd.DataFrame(high_low_data)
    df_with_hl = mark_highs_lows(df, 3, 3)

    assert df_with_hl["highLow"][3] == 1

def test_marks_low_point(high_low_data):
    high_low_data["low"] = [4, 3, 2, 1, 2, 3, 4]

    df = pd.DataFrame(high_low_data)
    df_with_hl = mark_highs_lows(df, 3, 3)

    assert df_with_hl["highLow"][3] == -1

def test_marks_high_low_point(high_low_data):
    high_low_data["high"] = [1, 2, 3, 4, 3, 2, 1]
    high_low_data["low"] = [4, 3, 2, 1, 2, 3, 4]

    df = pd.DataFrame(high_low_data)
    df_with_hl = mark_highs_lows(df, 3, 3)

    assert df_with_hl["highLow"][3] == 3

def test_only_marks_last_adjacent_high_with_same_value(high_low_data):
    high_low_data["high"] = [1, 2, 4, 4, 4, 2, 1]

    df = pd.DataFrame(high_low_data)
    df_with_hl = mark_highs_lows(df, 2, 2)

    assert df_with_hl["highLow"][2] == 0
    assert df_with_hl["highLow"][3] == 0
    assert df_with_hl["highLow"][4] == 1

def test_only_marks_last_adjacent_low_with_same_value(high_low_data):
    high_low_data["low"] = [4, 3, 1, 1, 1, 3, 4]

    df = pd.DataFrame(high_low_data)
    df_with_hl = mark_highs_lows(df, 2, 2)

    assert df_with_hl["highLow"][2] == 0
    assert df_with_hl["highLow"][3] == 0
    assert df_with_hl["highLow"][4] == -1
    