from data.binance.binance_api import get_klines_data
from unittest.mock import patch

import pytest

def test_successful_request_and_data_retrieval():
    trading_pair = "BTCUSDT"
    timeframe = "1h"
    candlestick_limit = 5
    mock_response_json = [[1690966800000, '29489.54000000', '29501.43000000', '29419.80000000', '29453.52000000', '1694.81848000', 1690970399999, '49931674.71823270', 28880, '633.35104000', '18654916.65394930', '0'], [1690970400000, '29453.52000000', '29534.33000000', '29442.00000000', '29527.93000000', '853.89192000', 1690973999999, '25175917.14116220', 20540, '480.14428000', '14156016.52062970', '0']]
    
    with patch("requests.get") as mock_get:
        # Set up the mock response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = mock_response_json

        response = get_klines_data(trading_pair, timeframe, candlestick_limit)

    assert response == mock_response_json

def test_invalid_timeframe_raises_value_error():
    trading_pair = "BTCUSDT"
    timeframe = "?h"
    candlestick_limit = 5

    with pytest.raises(ValueError):
        get_klines_data(trading_pair, timeframe, candlestick_limit)

# Test case for raising an exception for non 200 API response code
def test_invalid_api_response_raises_exception():
    trading_pair = "BTCUSDT"
    timeframe = "1h"
    candlestick_limit = 1
    mock_response_json = [[1690966800000, '29489.54000000', '29501.43000000', '29419.80000000', '29453.52000000', '1694.81848000', 1690970399999, '49931674.71823270', 28880, '633.35104000', '18654916.65394930', '0']]
    
    with patch("requests.get") as mock_get:
        # Set up the mock response
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.json.return_value = mock_response_json

        with pytest.raises(Exception):
            get_klines_data(trading_pair, timeframe, candlestick_limit)
