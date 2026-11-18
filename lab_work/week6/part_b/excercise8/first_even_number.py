def find_first_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
        # else: # This else statement was not needed and was inside the for loop. By putting the return outside the for loop, only when no even numbers are found, the function will return None
    return None


result = find_first_even_number([1, 3, 5, 6, 7, 8])
print(result)
