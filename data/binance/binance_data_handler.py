from data.data_handler_interface import DataHandlerInterface
from data.binance.binance_formatter import format_bincance
from data.binance.binance_api import get_klines_data

from data.price_data import PriceData

class BinanceDataHandeler(DataHandlerInterface):
    def __init__(self):
        self.valid_intervals = ["1s", "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"]

    def retrieve_data(self, trading_pair, interval, candlestick_limit):
        if interval not in self.valid_intervals:
            raise ValueError(f"invalid interval value: '{interval}'")
        
        price_data_json = get_klines_data(trading_pair, interval, candlestick_limit)
        formatted_price_data_df = format_bincance(price_data_json)

        price_data = PriceData(trading_pair)
        price_data.price_data_df = formatted_price_data_df

        return price_data
