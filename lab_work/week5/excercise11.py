def longest_consecutive(numbers):
    if not numbers:
        return 0

    sorted_nums = sorted(numbers)
    current = 1
    longest = 1

    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            current += 1                      # run continues
        elif sorted_nums[i] != sorted_nums[i - 1]:
            current = 1                       # run broke, start a new one
        # if equal (duplicate): do nothing
        longest = max(longest, current)

    return longest


print(longest_consecutive([100, 4, 200, 1, 3, 2]))          # 4
print(longest_consecutive([1, 2, 3, 4, 5]))                 # 5
print(longest_consecutive([10, 30, 20, 40]))                # 1
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(longest_consecutive([5, 5, 5, 5] ))                   # 1
