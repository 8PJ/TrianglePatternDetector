from detection.triangle_detector import TriangleDetector
from data.price_data import PriceData

import pandas as pd
import pytest
import json

@pytest.fixture
def triangle_detector_instance():
    triangle_detector = TriangleDetector()
    return triangle_detector

@pytest.fixture
def api_data():
    data = json.loads(r'[{"open":97,"close":100,"high":101,"low":96,"volume":2,"time":"2020-02-0614:30:00"},{"open":100,"close":102,"high":103,"low":99,"volume":2,"time":"2020-02-0614:30:00"},{"open":102,"close":103,"high":103,"low":101,"volume":2,"time":"2020-02-0614:30:00"},{"open":103,"close":104,"high":105,"low":102,"volume":2,"time":"2020-02-0614:30:00"},{"open":104,"close":101,"high":105,"low":100,"volume":2,"time":"2020-02-0614:30:00"},{"open":101,"close":98,"high":102,"low":98,"volume":2,"time":"2020-02-0614:30:00"},{"open":98,"close":95,"high":99,"low":94,"volume":2,"time":"2020-02-0614:30:00"},{"open":95,"close":96,"high":97,"low":93,"volume":2,"time":"2020-02-0614:30:00"},{"open":96,"close":90,"high":96,"low":88,"volume":2,"time":"2020-02-0614:30:00"},{"open":90,"close":87,"high":90,"low":86,"volume":2,"time":"2020-02-0614:30:00"},{"open":87,"close":88,"high":89,"low":85,"volume":2,"time":"2020-02-0614:30:00"},{"open":88,"close":87,"high":89,"low":86,"volume":2,"time":"2020-02-0614:30:00"},{"open":87,"close":93,"high":94,"low":86,"volume":2,"time":"2020-02-0614:30:00"},{"open":93,"close":92,"high":94,"low":91,"volume":2,"time":"2020-02-0614:30:00"},{"open":92,"close":95,"high":96,"low":92,"volume":2,"time":"2020-02-0614:30:00"},{"open":95,"close":99,"high":100,"low":94,"volume":2,"time":"2020-02-0614:30:00"},{"open":99,"close":103,"high":104,"low":98,"volume":2,"time":"2020-02-0614:30:00"},{"open":103,"close":104,"high":105,"low":101,"volume":2,"time":"2020-02-0614:30:00"},{"open":104,"close":97,"high":101,"low":96,"volume":2,"time":"2020-02-0614:30:00"},{"open":97,"close":96,"high":98,"low":96,"volume":2,"time":"2020-02-0614:30:00"},{"open":96,"close":97,"high":98,"low":94,"volume":2,"time":"2020-02-0614:30:00"},{"open":97,"close":92,"high":97,"low":91,"volume":2,"time":"2020-02-0614:30:00"},{"open":92,"close":90,"high":93,"low":89,"volume":2,"time":"2020-02-0614:30:00"},{"open":90,"close":91,"high":91,"low":90,"volume":2,"time":"2020-02-0614:30:00"},{"open":91,"close":93,"high":94,"low":89,"volume":2,"time":"2020-02-0614:30:00"},{"open":93,"close":92,"high":94,"low":91,"volume":2,"time":"2020-02-0614:30:00"},{"open":92,"close":95,"high":96,"low":92,"volume":2,"time":"2020-02-0614:30:00"},{"open":95,"close":100,"high":101,"low":94,"volume":2,"time":"2020-02-0614:30:00"},{"open":100,"close":104,"high":105,"low":100,"volume":2,"time":"2020-02-0614:30:00"},{"open":104,"close":95,"high":99,"low":95,"volume":2,"time":"2020-02-0614:30:00"},{"open":95,"close":96,"high":96,"low":94,"volume":2,"time":"2020-02-0614:30:00"},{"open":96,"close":97,"high":98,"low":95,"volume":2,"time":"2020-02-0614:30:00"},{"open":97,"close":95,"high":97,"low":94,"volume":2,"time":"2020-02-0614:30:00"},{"open":95,"close":94,"high":95,"low":93,"volume":2,"time":"2020-02-0614:30:00"},{"open":94,"close":95,"high":95,"low":93,"volume":2,"time":"2020-02-0614:30:00"},{"open":95,"close":96,"high":97,"low":94,"volume":2,"time":"2020-02-0614:30:00"},{"open":96,"close":97,"high":97,"low":95,"volume":2,"time":"2020-02-0614:30:00"},{"open":97,"close":98,"high":99,"low":96,"volume":2,"time":"2020-02-0614:30:00"}]')
    data = pd.json_normalize(data)

    price_data = PriceData("BTCUSDT")
    price_data.price_data_df = data

    return price_data

def test_triangle_detector_returns_triangle(triangle_detector_instance:TriangleDetector, api_data:PriceData):
    triangle = triangle_detector_instance.get_triangle_if_exists(api_data, 3, 3, 100)

    assert triangle is not None