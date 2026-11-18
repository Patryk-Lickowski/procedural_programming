import time

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# print(fibonacci_iterative(0))
# print(fibonacci_iterative(1))
# print(fibonacci_iterative(5))
# print(fibonacci_iterative(7))
# print(fibonacci_iterative(10))
start = time.perf_counter()
print(fibonacci_iterative(15))
end = time.perf_counter()
print(f'The iterative execution for n = 15 took {end - start} seconds')

start = time.perf_counter()
print(fibonacci_iterative(25))
end = time.perf_counter()
print(f'The iterative execution for n = 25 took {end - start} seconds')


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# print(fibonacci_recursive(0))
# print(fibonacci_recursive(1))
# print(fibonacci_recursive(5))
# print(fibonacci_recursive(7))
# print(fibonacci_recursive(10))
start = time.perf_counter()
print(fibonacci_recursive(15))
end = time.perf_counter()
print(f'The recursive execution for n = 15 took {end - start} seconds')

start = time.perf_counter()
print(fibonacci_recursive(25))
end = time.perf_counter()
print(f'The recursive execution for n = 25 took {end - start} seconds')
