numbers = [10, 20, 30, 40]
try:
    index = int(input("Enter an index number"))
    divisor = int(input("Enter a divisor"))
    result = numbers[index] / divisor
    print(f"Result: {result}")
except ValueError:
    print("ValueError: inputs have to be a number")
except IndexError:
    print("Input index out of range")
except ZeroDivisionError:
    print("Cannot divide by 0")
except Exception as e:
    print(f"Unknown error: {e}")
