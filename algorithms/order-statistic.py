from partition import hoare_partition

# The kth order statistic kth smallest element (1-indexed) in a list of numbers.
def quickselect(array: list, kth: int, left: int = 0, right: int = None):
    if kth < 1 or kth > len(array):
        return ValueError("Out of bounds")
    if right is None:
        right = len(array) - 1

    pivot_index = hoare_partition(array, left, right)
    if pivot_index == kth:
        return array[pivot_index]
    elif kth < pivot_index:
        return quickselect(array, kth, left, pivot_index - 1)
    else:
        kth -= pivot_index + 1
        return quickselect(array, kth, pivot_index + 1, right)






