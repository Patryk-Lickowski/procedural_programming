def login_system():
    username = 'student'
    password = 'python123'

    username_input = str(input("Enter your username: "))
    password_input = str(input("Enter your password: "))

    if username_input == username and password_input == password:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("Access Granted")
        else:
            print("You must be at least 18.")
    elif username_input == username and password_input != password:
        print("Username recognised.")
        login_system()
    elif username_input != username and password_input == password:
        print("Password recognised.")
        login_system()
    else:
        print("Unknown error")
        login_system()


login_system()