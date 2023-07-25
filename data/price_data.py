# holds the pandas dataframe containing price data
class PriceData:
    def __init__(self, ticker):
        self._price_data = None
        self._ticker = ticker

    # ticker

    @property
    def ticker(self):
        return self._ticker

    # price data

    @property
    def price_data(self):
        return self._price_data
    
    @price_data.setter
    def price_data(self, price_df):
        self._price_data = price_df
