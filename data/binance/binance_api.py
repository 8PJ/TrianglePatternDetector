from ratelimit import limits, sleep_and_retry

import requests

valid_intervals = ["1s", "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"]
klines_url = "https://api.binance.com/api/v3/klines"

def get_klines_data(trading_pair, timeframe, candlestick_limit):
    # check if timeframe is valid
    if timeframe not in valid_intervals:
        raise ValueError(f"invalid timeframe value: '{timeframe}'")

    # api requests are limited to 1000 candlesticks
    candlestick_limit = min(candlestick_limit, 1000)

    params = {"symbol": trading_pair, "interval": timeframe, "limit": 1000}
    response = make_binance_api_request(klines_url, params=params)

    if response.status_code != 200:
        raise Exception("Error retrieving klines data: " + response.text)
    
    return response.json()
        

@sleep_and_retry
@limits(calls=1100, period=61)
def make_binance_api_request(url, params):
    while True:
        try:
            response = requests.get(url, params)
            return response
        except Exception as e:
            print("full exception:\n" + str(e))
            continue
