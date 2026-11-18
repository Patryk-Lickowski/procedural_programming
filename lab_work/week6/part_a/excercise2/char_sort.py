def char_sort(word):

    # Sort using a tuple key: (lowercase_char, is_lowercase_boolean)
    sorted_chars = sorted(word, key=lambda char: (char.lower(), char.islower()))

    # Join the list back into a single string
    result = "".join(sorted_chars)

    return result
