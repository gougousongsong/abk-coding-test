import pytest
from src.math_utils import fibonacci


def test_fibonacci_base_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55


def test_fibonacci_larger_values():
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040


def test_fibonacci_negative_error():
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci(-10)


def test_fibonacci_invalid_type_error():
    with pytest.raises(TypeError):
        fibonacci(3.14)
    with pytest.raises(TypeError):
        fibonacci("5")
    with pytest.raises(TypeError):
        fibonacci(None)
    with pytest.raises(TypeError):
        fibonacci(True)
