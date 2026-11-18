import pytest
from num_prod import *

def test_num_prod():
    # Testing 2 positive numbers
    assert num_prod(3, 4) == 12

    # Testing 2 negative numbers
    assert num_prod(-4, -9) == 36

    # Testing on mix of numbers
    assert num_prod(6, -3) == -18

    # Testing with 0 on the right
    assert num_prod(-4, 0) == 0

    # Testing with 0 on the left
    assert num_prod(0, 4) == 0

    # Testing with non numeric inputs
    assert num_prod("abc", "xyz") == None

pytest.main()
