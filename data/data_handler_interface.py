from abc import ABC, abstractmethod

class DataHandlerInterface(ABC):
    @abstractmethod
    def retrieve_data(self, ticker, timeframe, candlestick_limit):
        pass
