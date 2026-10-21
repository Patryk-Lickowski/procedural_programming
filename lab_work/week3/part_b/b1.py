def ride_check():
    age = int(input("How old are you?: "))
    height = int(input("How tall are you? (cm): "))

    if age < 12:
        print("You are too young to go on this ride.")
        ride_check()
    elif height >= 140:
        print("You can go on the ride!")
        ride_check()
    elif height < 140:
        print("You do not meet the height requirement.")
        ride_check()
    else:
        print("Invalid age or height entered.")
        ride_check()

ride_check()


