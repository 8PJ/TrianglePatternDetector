def get_max_triangle_len():
    max_triangle_len = None
    max_triangle_len_str = input(f"Please enter a maximum length of a triangle (in candlesticks): ")

    while max_triangle_len is None:
        try:
            max_triangle_len = int(max_triangle_len_str)
        except ValueError:
            max_triangle_len_str = input(f"Could not recognise {max_triangle_len_str} as an integer, please enter a maximum length of a triangle (in candlesticks): ")

    return max_triangle_len