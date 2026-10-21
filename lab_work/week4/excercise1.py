def find_all_even_for_loop():
    print("FOR LOOP")
    for i in range (1, 22):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")


def find_all_event_while_loop():
    x = 0
    print("WHILE LOOP")
    while x != 20:
        if x % 2 == 0:
            print(f"{x} is even")
        else:
            print(f"{x} is odd")
        x += 1

find_all_even_for_loop()
find_all_event_while_loop()
