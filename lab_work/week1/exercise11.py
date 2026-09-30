def odd_even(number):
    return 'Even' if number % 2 == 0 else 'Odd'

while True:
    try:
        number = int(input('Enter an integer number: '))
        break
    except ValueError:
        print('You need to enter an integer')

print(odd_even(number))