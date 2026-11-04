def two_sum(num_list, target):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == target:
                return[i, j]

list = [1, 2, 4, 6, 8, 11]
print(two_sum(list, 12))
