def int_factorial():
    total = 0
    x = int(input("Enter a positive integer: "))
    if x < 0:
        print("Invalid integer input")
    else:
        for i in range(1, x):
            total = i * (i + 1)
    print(total)
int_factorial()
