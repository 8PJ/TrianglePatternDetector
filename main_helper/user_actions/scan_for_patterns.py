from detection.triangle_detector import TriangleDetector
from main_helper.user_options import UserOptions
import concurrent.futures


def scan_for_patterns(options: UserOptions):
    price_data_map = get_price_data_map(options)
    scan_results_map = perform_scan(options, price_data_map)

    for (ticker, interval), triangle in scan_results_map.items():
        print(f"{ticker} ({interval}):")

        if triangle is None:
            print("- not found")
        else:
            print(triangle)
            # print(f"- Found at: {triangle.start_datetime}, type: {triangle.type_string}")

        print("")


def get_price_data_map(options: UserOptions):
    futures = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        for ticker in options.tickers:
            for interval in options.intervals:
                key = (ticker, interval)

                future = executor.submit(
                    options.data_handler.retrieve_data,
                    ticker,
                    interval,
                    options.candlestick_limit,
                )
                futures.append((key, future))

    price_data_map = dict()

    for key, future in futures:
        price_data_map[key] = future.result()

    return price_data_map


def perform_scan(options: UserOptions, price_data_map):
    futures = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=32) as executor:
        for key in price_data_map:
            future = executor.submit(
                TriangleDetector.get_triangle_if_exists,
                price_data_map[key],
                options.hl_num_before,
                options.hl_num_after,
                options.max_triangle_len,
            )
            futures.append((key, future))

    scan_results_map = dict()

    for key, future in futures:
        scan_results_map[key] = future.result()

    return scan_results_map
