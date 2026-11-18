import pytest
from char_sort import *


def test_char_sort():
    # Testing on a random word
    assert char_sort('programming') == 'aggimmnoprr'

    # Testing on a word with different letters
    assert char_sort('civic') == 'cciiv'

    # Testing on an already sorted word
    assert char_sort('aabb') == 'aabb'

    # Testing on a word with capital and small letters
    assert char_sort('PaBaBB') == 'aaBBBP'

    # Testing on a mix of uppercase and lowercase letters
    assert char_sort('BaAaA') == 'AAaaB'

pytest.main()
