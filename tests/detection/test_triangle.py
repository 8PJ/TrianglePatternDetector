from detection.triangle import Triangle

import pytest

@pytest.fixture
def triangle_instance():
    triangle = Triangle(0, 50, 50, 10, 30, 30, 0)
    return triangle

def test_returns_correct_list_of_xs(triangle_instance:Triangle):
    xs = triangle_instance.get_xs()
    
    assert xs == [0, 50]

def test_returns_correct_list_of_high_ys(triangle_instance:Triangle):
    xs = triangle_instance.get_high_ys()
    
    assert xs == [50, 30]

def test_returns_correct_list_of_low_ys(triangle_instance:Triangle):
    xs = triangle_instance.get_low_ys()
    
    assert xs == [10, 30]

def test_rejects_invalid_triangle_type():
    with pytest.raises(ValueError):
        Triangle(0, 50, 50, 10, 30, 30, 2)