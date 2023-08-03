def get_hl_num_before():
    hl_num_before = None
    hl_num_before_str = input(f"Please enter a number of preceding candlesticks to use in high/low detection: ")

    while hl_num_before is None:
        try:
            hl_num_before = int(hl_num_before_str)
        except ValueError:
            hl_num_before_str = input(f"Could not recognise {hl_num_before_str} as an integer, please enter a number of preceding candlesticks to use in high/low detection: ")

    return hl_num_before