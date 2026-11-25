import random
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort

numbers = random.sample(range(1, 101), 20)

bubble_sort_ops = bubble_sort(numbers.copy())
insertion_sort_ops = insertion_sort(numbers.copy())
selection_sort_ops = selection_sort(numbers.copy())

print(f"\n\nThe dataset is {numbers}")
print(f"The bubble sort sorted the list within {bubble_sort_ops} swaps.\nThe insertion sort sorted the list within {insertion_sort_ops} shifts.\nThe selection sort ordered the list within {selection_sort_ops} swaps.\n\n")
