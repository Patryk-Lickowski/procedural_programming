import pytest
from movie_ticket_price import *

def test_movie_ticket_price():
    # One adult at 10 AM
    assert movie_ticket_price(0, 1, 0, 10) == 14.25

    # Two children and two adults at 5 PM
    assert movie_ticket_price(2, 2, 0, 17) == 30

    # Two children and two adults at 1 PM
    assert movie_ticket_price(2, 2, 0, 13) == 28.50

    # Two children, one adult and one senior at 1 PM
    assert movie_ticket_price(2, 1, 1, 13) == 30.40

    # Three children, two adults and one senior at 2 PM
    assert movie_ticket_price(3, 2, 1, 14) == 38.95

    # Three children, one adult and two seniors at 3 PM
    assert movie_ticket_price(3, 1, 2, 15) == 49

    # Four children, three adults and two seniors at 11 AM
    assert movie_ticket_price(4, 3, 2, 11) == 69.35

    # Negative input is provided
    assert movie_ticket_price(-2, 5, 6, 2) == None

    # Negative input is provided
    assert movie_ticket_price(2, -5, 6, 2) == None

    # Negative input is provided
    assert movie_ticket_price(2, 5, -6, 2) == None

    # Negative input is provided
    assert movie_ticket_price(2, 5, 6, -2) == None

pytest.main()
