def float_range(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step


def discount_calc():
    amount = float(input("Enter the cost before any discounts (2d.p. eg. 23.00): "))
    if amount < 50:
        print(f"There is no discount applied, total is: £{amount}")
    elif amount in float_range(50, 99.99, 0.01):
        print(f"Original amount: £{amount}")
        print(f"Discount: £{amount * 0.1}")
        print(f"A 10% discount has been applied, total is: £{amount * 0.9}")
    elif amount > 100:
        print(f"Original amount: £{amount}")
        print(f"Discount: £{amount * 0.2}")
        print(f"A 20% discount has been applied, total is: £{amount * 0.8}")
        
discount_calc()
