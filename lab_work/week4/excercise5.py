def square_up():
    target = int(input("Enter the number you want to square up to: "))
    for i in range(1, target + 1):
        print(i ** 2)

square_up()
