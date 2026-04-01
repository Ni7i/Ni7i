"""Tests for sorting algorithms."""
import sys
import random
sys.path.insert(0, "..")

from src.algorithms.sorting import *


def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    print("bubble_sort: OK")


def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    random_arr = [random.randint(0, 100) for _ in range(50)]
    assert merge_sort(random_arr) == sorted(random_arr)
    print("merge_sort: OK")


if __name__ == "__main__":
    test_bubble_sort()
    test_merge_sort()
    print("All sorting tests passed!")
