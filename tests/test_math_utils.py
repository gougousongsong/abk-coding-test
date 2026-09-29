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
    # 测试正常情况 (0, 1, 5, 10)
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

    # 测试负数边界情况 (必须抛出指定消息的 ValueError)
    try:
        fibonacci(-1)
        assert False, "Expected ValueError for negative input"
    except ValueError as e:
        assert str(e) == "n must be non-negative"

    try:
        fibonacci(-10)
        assert False, "Expected ValueError for negative input"
    except ValueError as e:
        assert str(e) == "n must be non-negative"