def recursive_max(arr: list[int]) -> int:
    """Returns the max element in a list
    of numbers
    """

    if len(arr) == 0:
        return None

    if len(arr) == 1:
        return arr[0]

    first = arr[0]

    # max element in sub array
    max_sub = recursive_max(arr[1:])

    return first if first > max_sub else max_sub
