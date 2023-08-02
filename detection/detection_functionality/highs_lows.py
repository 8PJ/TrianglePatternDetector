def mark_highs_lows(df, num_before, num_after):
    df_copy = df.copy()

    if len(df_copy) == 0:
        df_copy["high_low"] = []
    else:
        df_copy["high_low"] = df_copy.apply(
            lambda row: check_high_low(df_copy, row.name, num_before, num_after), axis=1
        )

    return df_copy

def check_high_low(df, candlestick_num, num_before, num_after):
    # if tested candlestick is out of bounds of data
    if (
        candlestick_num - num_before < df.iloc[0].name
        or candlestick_num + num_after > df.iloc[-1].name
    ):
        return 0

    # find high/low of the interval (not including the current candlestick)
    intervalLowBefore = df.iloc[candlestick_num - num_before : candlestick_num - 1]["low"].min()
    intervalLowAfter = df.iloc[candlestick_num + 1 : candlestick_num + num_after]["low"].min()

    intervalHighBefore = df.iloc[candlestick_num - num_before : candlestick_num - 1]["high"].max()
    intervalHighAfter = df.iloc[candlestick_num + 1 : candlestick_num + num_after]["high"].max()

    # a candlestick is a low when it's low price is lower or equal than neighbours to the left and
    # lower (not equal) than neighbours to the right
    # similarly for high
    isLow = (
        intervalLowBefore >= df.iloc[candlestick_num]["low"]
        and intervalLowAfter > df.iloc[candlestick_num]["low"]
    )
    isHigh = (
        intervalHighBefore <= df.iloc[candlestick_num]["high"]
        and intervalHighAfter < df.iloc[candlestick_num]["high"]
    )

    if isLow and isHigh:
        return 3
    elif isHigh:
        return 1
    elif isLow:
        return -1
    else:
        return 0