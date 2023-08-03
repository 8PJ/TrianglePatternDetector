def get_candlestick_limit():
    candlestick_limit = None
    candlestick_limit_str = input(f"Please enter a candlestick limit used for pattern detection: ")

    while candlestick_limit is None:
        try:
            candlestick_limit = int(candlestick_limit_str)
        except ValueError:
            candlestick_limit_str = input(f"Could not recognise {candlestick_limit_str} as an integer, please enter a candlestick limit: ")

    return candlestick_limit