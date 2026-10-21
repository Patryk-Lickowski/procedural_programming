def profile_builder():
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    favourite_lang = str(input("Enter your favourite programming language: "))

    add_msg = favourite_lang.lower() == 'python'

    print(f"Hello, {name}!")

    if age >= 18:
        print("Keep developing your programming skills!")
    elif age in range(0, 19):
        print("You are still learning and developing your skills.")
    else:
        print("Invalid age entered")
    
    if add_msg:
        print("Python is a great language to learn!")


profile_builder()
    