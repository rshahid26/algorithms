from .partition import hoare_partition, lomuto_partition

# The kth order statistic of a list of numbers is the (1-indexed) kth smallest element.


def quickselect(array, kth: int):
    """
    Partition the array with Lomuto s.t. the integer at the pivot
    index is in its final sorted location. Then, array[pivot] is
    the (pivot-index + 1)th smallest integer.

    Use this to determine which subarray to recurse in for k.
    Average case O(n)
    Worst case O(n^2)
    """
    if kth <= 0 or kth > len(array):
        return "k out of bounds"
    def qs(left: int, right: int):
        pivot_index = lomuto_partition(array, left, right)
        if kth == pivot_index + 1: # account for 1-indexed
            return array[pivot_index]
        elif kth < pivot_index + 1:
            return qs(left, pivot_index - 1)
        else:
            return qs(pivot_index + 1, right)

    return qs(0, len(array) - 1)

