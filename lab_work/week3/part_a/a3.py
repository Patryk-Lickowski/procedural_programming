def guessing_game():
    secret_number = 7

    
    guess = int(input("Guess the number: "))
    
    if guess == secret_number:
        print(f"Congratulations, {secret_number} was the secret number!")
    elif guess > secret_number:
        print("Too High!")
        guessing_game()
    elif guess < secret_number:
        print("Too Low!")
        guessing_game()


guessing_game()