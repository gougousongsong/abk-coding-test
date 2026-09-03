import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from math_utils import add, multiply, fibonacci

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_fibonacci_normal_cases():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_larger_values():
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765
