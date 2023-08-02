from data.binance.binance_data_handler import BinanceDataHandeler

def get_data_handler():
    available_data_sources = {"crypto": BinanceDataHandeler}

    selection = input(f"Please select a data source. Available data sources: {list(available_data_sources.keys())}: ")

    while selection not in available_data_sources:
        selection = input(f"Data source not recognised, please select one of {list(available_data_sources.keys())}: ")

    data_handler = available_data_sources[selection]()

    return data_handler