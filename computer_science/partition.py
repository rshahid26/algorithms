def lomuto_partition(array: list, left: int = 0, right: int = None):
    """
    Partition the subarray [left, right] in place such that:
                     < pivot       pivot         >= pivot
    [left, right] = [left, i] + array[right] + [i + 2, right]

    By iterating from j in [left, right) and swapping array[j] to
    array[i], the right-bound of the < subarray, if array[j] < pivot.
    Finally, swap the pivot to its new location, array[i + 1].
    """
    if right is None:
        right = len(array) - 1

    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

def hoare_partition(array: list, left: int = 0, right: int = None):
    """
    Partition the subarray [left, right] in place such that:
                     <= pivot      >= pivot
    [left, right] = [left, j] + [j + 1, right]

    By iterating i while [left, i] < pivot and decrementing j while
    [j, right] > pivot. When both conditions are false, array[i] and
    array[j] can be swapped and i and j will continue to get closer.

    This terminates when j crosses into [left, i]. j is returned as
    the pivot index but this is not necessarily the chosen pivot or
    in its final sorted location like with lomuto partitioning.
    """
    if right is None:
        right = len(array) - 1

    pivot = array[left]
    i, j = left - 1, right + 1

    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j
        # May swap the pivot into [j + 1, right]
        array[i], array[j] = array[j], array[i]
