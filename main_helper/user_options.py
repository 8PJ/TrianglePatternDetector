from TrianglePatternDetector.main_helper.user_input import get_intervals
from main_helper.user_input.get_data_handler import get_data_handler
from main_helper.user_input.get_tickers import get_tickers

class UserOptions:
    def __init__(self):
        self.data_handler = None
        self.tickers = None
        self.intervals = None
        self.candlestick_limit = None
        self.hl_num_before = None
        self.hl_num_after = None
        self.max_triangle_len = None

    def initialise_options(self):
        self.data_handler = get_data_handler()
        self.tickers = get_tickers()
        self.timeframes = get_intervals(self.data_handler.valid_intervals)