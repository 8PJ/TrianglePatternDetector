from main_helper.user_input.get_candlestick_limit import get_candlestick_limit
from main_helper.user_input.get_max_triangle_len import get_max_triangle_len
from main_helper.user_input.get_hl_num_before import get_hl_num_before
from main_helper.user_input.get_hl_num_after import get_hl_num_after
from main_helper.user_input.get_data_handler import get_data_handler
from main_helper.user_input.get_intervals import get_intervals
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
        self.intervals = get_intervals(self.data_handler.valid_intervals)
        self.candlestick_limit = get_candlestick_limit()
        self.hl_num_before = get_hl_num_before()
        self.hl_num_after = get_hl_num_after()
        self.max_triangle_len = get_max_triangle_len()

    def reinitialise_options(self):
        pass # TODO
    