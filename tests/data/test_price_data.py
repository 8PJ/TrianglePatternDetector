from data.price_data import PriceData

import pandas as pd
import pytest

def test_undefined_ticker_raises_value_error():
    with pytest.raises(ValueError):
        PriceData(None)

def test_price_data_df_is_initialised_to_none():
    price_data = PriceData("BTCUSDT")

    assert price_data.price_data_df is None

def test_price_data_df_can_be_set():
    price_data = PriceData("BTCUSDT")

    test_df = pd.DataFrame()

    price_data.price_data_df = test_df

    assert price_data.price_data_df is not None