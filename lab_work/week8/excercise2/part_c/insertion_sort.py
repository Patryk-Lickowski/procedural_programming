def insertion_sort(arr):
    shift = 0
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
            shift += 1

        arr[j + 1] = current_value
    return shift
