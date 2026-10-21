def sum_of_even_not_div_three():
    total = 0
    for i in range(0, 100):
        if i % 2 == 0:
            if i % 3 != 0:
                total += i

    print(total)

sum_of_even_not_div_three()
