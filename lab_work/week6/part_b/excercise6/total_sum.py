def total_sum(lst):
    total = 0 # Because the total was inside the for loop, for every iteration of the loop it was resetting to 0
    for x in lst:
        total = x + total
    return total

# run the function
print(total_sum([1, 2, 3, 4])) # Expected output is 10
