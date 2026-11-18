# def factorial_iterative(n):
#     result = n
#     for i in range(1, n):
#         result *= i
#     return result

# print(factorial_iterative(0))
# print(factorial_iterative(1))
# print(factorial_iterative(3))
# print(factorial_iterative(5))
# print(factorial_iterative(7))


def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(0))
print(factorial_recursive(1))
print(factorial_recursive(3))
print(factorial_recursive(5))
print(factorial_recursive(7))
