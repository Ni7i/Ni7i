"""Tests for math helper functions."""
import sys
sys.path.insert(0, "..")

from src.utils.math_helpers import *


def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
    print("fibonacci: OK")


def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(17)
    assert not is_prime(15)
    print("is_prime: OK")


if __name__ == "__main__":
    test_fibonacci()
    test_is_prime()
    print("All math tests passed!")
