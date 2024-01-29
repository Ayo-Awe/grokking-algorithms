
def selection_sort(arr: list[int]):
    """Sorts an array of numbers in place in ascending
    order using selection sort
    """
    arr_len = len(arr)

    # sort array in ascending order
    for i in range(arr_len):
        for j in range(i+1, arr_len):

            if arr[j] < arr[i]:
                swap(arr, i, j)


def swap(arr: list[int], i: int, j: int):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp
