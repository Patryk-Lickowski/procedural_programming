def find_all_div_six():
    div_six = []
    for i in range(0, 101):
        if i % 6 == 0:
            div_six.append(i)

    print(div_six)

find_all_div_six()
