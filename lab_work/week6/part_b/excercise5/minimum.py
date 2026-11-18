def minimum(lst):
    a = 0
    for x in range(1, len(lst)):
        if lst[x] < lst[a]:
            a = x
    return lst[a] # This was returning the index of the value as opposed to the value itself


print(minimum([4, 2, 7, 3])) # The output should be 2
