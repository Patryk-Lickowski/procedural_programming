def movie_ticket_price(num_children, num_adults, num_seniors, show_time):
    if num_adults < 0 or num_children < 0 or num_seniors < 0 or show_time < 0:
        return None

    adult_price = 15
    senior_price = 12
    child_price = 5
    has_senior_discount = False

    # 1. Group Size Discounts
    if num_adults >= 2:
        num_children -= 2
        if num_seniors >= 1:
            has_senior_discount = True
    elif num_seniors >= 1:
        num_children -= 1

    # 2. Time-Based Discount
    if show_time < 15:
        adult_price *= 0.95
        senior_price *= 0.95
        child_price *= 0.95

    if num_children < 0:
        num_children = 0

    # 3. Calculate base totals
    total = (adult_price * num_adults) + (senior_price * num_seniors) + (child_price * num_children)

    # 4. Apply the half-price discount to exactly ONE senior if eligible
    if has_senior_discount:
        total -= (senior_price * 0.5)

    return round(total, 2)
