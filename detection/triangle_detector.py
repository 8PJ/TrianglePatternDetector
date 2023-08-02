from detection.detection_functionality.highs_lows import mark_highs_lows
from detection.detection_functionality.triangle_check import get_triangle

class TriangleDetector:
    def get_triangle_if_exists(self, price_data, hl_num_before, hl_num_after, max_triangle_len):
        price_data_with_hl = mark_highs_lows(price_data.price_data_df, hl_num_before, hl_num_after)

        triangle = get_triangle(price_data_with_hl, max_triangle_len)

        return triangle