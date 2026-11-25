def insertion_sort(arr):
    shift = 0
    for i in range(1, len(arr)):
        print(f"Pass {i}: {arr}")
        current_value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
            shift += 1

        arr[j + 1] = current_value

    print(f"Final sorted: {arr}")
    print(f"Total shifts: {shift}")
    return arr, shift

# print(insertion_sort([9, 4, 6, 2, 7]))
# print(insertion_sort([1, 2, 3, 4, 5]))
