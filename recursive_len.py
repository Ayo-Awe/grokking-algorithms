def recursive_len(arr: list[any]) -> int:
    """Recursive implementation of the len function
    """

    try:
        # pop off the first element in the arr
        arr.pop(0)

        return 1 + recursive_len(arr)
    except IndexError:
        # empty array
        return 0
