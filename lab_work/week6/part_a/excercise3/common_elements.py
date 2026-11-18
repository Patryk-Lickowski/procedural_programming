def common_elements(list_a, list_b):

    found = []
    # Loop directly through the numbers in list_a
    for item in list_a:
        # Check if that number exists anywhere inside the list_b
        if item in list_b:
            found.append(item)

    return sorted(found)
