def get_hl_num_after():
    hl_num_after = None
    hl_num_after_str = input(f"Please enter a number of succeeding candlesticks to use in high/low detection: ")

    while hl_num_after is None:
        try:
            hl_num_after = int(hl_num_after_str)
        except ValueError:
            hl_num_after_str = input(f"Could not recognise {hl_num_after_str} as an integer, please enter a number of succeeding candlesticks to use in high/low detection: ")

    return hl_num_after