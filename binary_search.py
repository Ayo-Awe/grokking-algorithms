from typing import Union


def binary_search(arr: list[int], item) -> Union[int, None]:
    # empty array
    if len(arr) == 0:
        return None

    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2

    # target found
    if item == arr[mid]:
        return mid

    new_start = None
    new_end = None
    new_arr = None

    # search right half
    if item > arr[mid]:
        new_start = mid + 1
        new_end = end
        new_arr = arr[new_start:new_end+1]

    # search left half
    elif item < arr[mid]:
        new_start = start
        new_end = mid - 1
        new_arr = arr[new_start:new_end+1]

    # recursively search new sub array
    idx = binary_search(new_arr, item)
    return idx + new_start if idx is not None else None
