def selection_sort(arr):
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
        print(arr)
    return arr, swaps

# print(selection_sort([25, 64, 11, 22, 12]))
# print(selection_sort([64, 25, 22, 12, 11]))
