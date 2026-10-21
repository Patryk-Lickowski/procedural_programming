def movie_check():
    age = int(input("How old are you?: "))
    if age >= 18:
        print('You can watch any age rated film.')
        movie_check()
    elif age in range (15, 18):
        print('You can watch a 15+ film.')
        movie_check()
    elif age in range(12, 15):
        print('You can watch a 12+ film.')
        movie_check()
    elif age < 12:
        print("You can watch any children's film")
        movie_check()
    else:
        print("Error, input couldn't be computed")
        movie_check()


movie_check()