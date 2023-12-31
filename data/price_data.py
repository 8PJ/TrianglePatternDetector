import pandas as pd

# holds the pandas dataframe containing price data
class PriceData:
    def __init__(self, ticker):
        if ticker == None:
            raise ValueError("ticker must be defined")
        
        self._ticker = ticker
        self._price_data_df = None

    # ticker

    @property
    def ticker(self):
        return self._ticker

    # price data

    @property
    def price_data_df(self):
        return self._price_data_df
    
    @price_data_df.setter
    def price_data_df(self, price_df):
        if isinstance(price_df, pd.DataFrame):
            self._price_data_df = price_df
        else:
            raise TypeError("price_data must be of type pandas.DataFrame")
