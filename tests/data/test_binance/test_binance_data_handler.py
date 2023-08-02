from data.binance.binance_data_handler import BinanceDataHandeler

from unittest.mock import patch
import pytest

@pytest.fixture
def data_handler_instance():
    data_handler = BinanceDataHandeler()
    return data_handler

def test_invalid_timeframe_raises_value_error(data_handler_instance):
    trading_pair = "BTCUSDT"
    timeframe = "?h"
    candlestick_limit = 5

    with pytest.raises(ValueError):
        data_handler_instance.retrieve_data(trading_pair, timeframe, candlestick_limit)

def test_returned_price_data_has_correct_trading_pair(data_handler_instance):
    trading_pair = "BTCUSDT"
    timeframe = "1h"
    candlestick_limit = 5
    mock_response_json = [[1690966800000, '29489.54000000', '29501.43000000', '29419.80000000', '29453.52000000', '1694.81848000', 1690970399999, '49931674.71823270', 28880, '633.35104000', '18654916.65394930', '0'], [1690970400000, '29453.52000000', '29534.33000000', '29442.00000000', '29527.93000000', '853.89192000', 1690973999999, '25175917.14116220', 20540, '480.14428000', '14156016.52062970', '0']]

    with patch("requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_json

        price_data = data_handler_instance.retrieve_data(trading_pair, timeframe, candlestick_limit)

        assert price_data.ticker == "BTCUSDT"

def test_returned_price_data_has_populated_data(data_handler_instance:BinanceDataHandeler):
    trading_pair = "BTCUSDT"
    timeframe = "1h"
    candlestick_limit = 5
    mock_response_json = [[1690966800000, '29489.54000000', '29501.43000000', '29419.80000000', '29453.52000000', '1694.81848000', 1690970399999, '49931674.71823270', 28880, '633.35104000', '18654916.65394930', '0'], [1690970400000, '29453.52000000', '29534.33000000', '29442.00000000', '29527.93000000', '853.89192000', 1690973999999, '25175917.14116220', 20540, '480.14428000', '14156016.52062970', '0']]

    with patch("requests.get") as mock_get:
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_json

        price_data = data_handler_instance.retrieve_data(trading_pair, timeframe, candlestick_limit)

        assert price_data.price_data_df is not None
