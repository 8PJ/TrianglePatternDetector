import pandas as pd
import datetime

def format_bincance(candlestick_data):
    processed_json = []

    # process every candlestick into 
    for candlestick in candlestick_data:
        processed_candlestick = {
            "open": float(candlestick[1]),
            "close": float(candlestick[4]),
            "high": float(candlestick[2]),
            "low": float(candlestick[3]),
            "volume": float(candlestick[7]),
            "number_transactions": float(candlestick[8]),
            "time": str(datetime.fromtimestamp(candlestick[0] / 1000))
        }

        processed_json.append(processed_candlestick)

    price_data_df = pd.json_normalize(processed_json)

    return price_data_df