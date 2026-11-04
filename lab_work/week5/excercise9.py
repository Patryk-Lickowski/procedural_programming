def print_pyramid(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


# Example usage
n = int(input("Enter the height of the pyramid: "))
print_pyramid(n)
