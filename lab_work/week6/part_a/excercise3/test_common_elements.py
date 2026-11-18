import pytest
from common_elements import *

def test_common_elements():
    # Testing two lists of different sizes
    assert common_elements([1, 2, 3, 4], [3, 4, 19, 21, 5]) == [3, 4]

    # Testing with no common elements
    assert common_elements([3, 3, 3], [4, 4, 4]) == []

    # Testing when all elements are common
    assert common_elements([3, 4, 5], [3, 4, 5]) == [3, 4, 5]

    # Testing with two common elements
    assert common_elements([11, 10, 9, 23], [23, 11, 15]) == [11, 23]

    # Testing with positive and negative numbers
    assert common_elements([-11, 11, -9, 10, 8], [10, -3, 0, 14, 8, -9]) == [-9, 8, 10]

pytest.main()
