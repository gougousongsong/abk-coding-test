import pytest
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

def test_fibonacci():
    """Verify fibonacci calculation for standard non-negative indices."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_fibonacci_negative():
    """Verify fibonacci raises ValueError with exact message for negative inputs."""
    with pytest.raises(ValueError, match="^n must be non-negative$"):
        fibonacci(-1)
    with pytest.raises(ValueError, match="^n must be non-negative$"):
        fibonacci(-10)
