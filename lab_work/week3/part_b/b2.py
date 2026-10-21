def number_check():
    num = int(input("Enter a number: "))

    if num == 0:
        print("This number is 0.")
        number_check()
    elif num < 0:
        print("This number is negative.")
        number_check()
    elif num > 0:
        print("This number is positive.")
        if num >= 100:
            print("This is a large number.")
            number_check()
        number_check()
    else:
        print("Invalid entry")


number_check()