from data.data_handler_interface import DataHandlerInterface
from data.binance.binance_formatter import format_bincance
from data.binance.binance_api import get_klines_data

from data.price_data import PriceData

class BinanceDataHandeler(DataHandlerInterface):
    def retrieve_data(self, trading_pair, timeframe, candlestick_limit):
        price_data_json = get_klines_data(trading_pair, timeframe, candlestick_limit)
        formatted_price_data_df = format_bincance(price_data_json)

        price_data = PriceData(trading_pair)
        price_data.price_data_df = formatted_price_data_df

        return price_data
