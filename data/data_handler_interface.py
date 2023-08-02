from abc import ABC, abstractmethod

class DataHandlerInterface(ABC):
    @abstractmethod
    def retrieve_data(self, ticker, interval, candlestick_limit):
        pass
