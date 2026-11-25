def bubble_sort(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
        print(f"Pass {i+1}")
        print(arr)
    return arr, swaps


# print(bubble_sort([0, 3, 6, 2, 8, 1]))
# print(bubble_sort([1, 2, 3, 4, 5]))
# print(bubble_sort([5, 4, 3, 2, 1]))
