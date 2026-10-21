def second_div_thirteen():
    found = 0
    for i in range(2000, 3000):
        if i % 13 == 0:
            found += 1
            if found == 2:
                print(i)

second_div_thirteen()
