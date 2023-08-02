import json

def get_tickers():
    tickers = None
    ticker_file = input(f"Please specify a json file with a list of tickers: ")

    while tickers is None:
        try:
            with open(ticker_file, "r") as user_file:
                content = user_file.read()
                tickers = json.loads(content)
        except FileNotFoundError:
            ticker_file = input(f"Could not find file called {ticker_file}, please specify a json file with a list of tickers: ")

    return tickers