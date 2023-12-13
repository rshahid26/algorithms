import random


# Backward traversal
def sort_bf(array):
    """
    Sorts in worst case O(n^2) by iterating through an array
    and bringing the greatest element [j] < i to the front
    with each new element i.
    """
    for i in range(len(array)):
        for j in range(i):

            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]

    return ''.join(array)


# Forward traversal
def selection_sort(array):
    """
    Sorts all cases in O(n^2) by iterating through an array
    and bringing the least element [j] > i to the back
    with each new element i.
    """
    for i in range(len(array)):
        for j in range(i, len(array), 1):

            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

    if isinstance(array, str):
        return ''.join(array)
    return array


def insertion_sort(array):
    """
    Sorts in worse case O(n^2) by iterating through an array
    and shifting all greater elements [j] < i to [j+1] until
    the right spot for the element i is found.
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
    return ''.join(array)


def mergesort(array: list, left: int = None, right: int = None):
    """
    Sorts an array by repeatedly dividing it in half. The two
    pieces are then combined  in O(n) time using two pointers.
    T(n) = 2T(ceil(n/2)) + O(n) = O(nlogn) time complexity.
    """
    if left is None or right is None:
        left, right = 0, len(array) - 1
    if left >= right:
        return [array[left]]

    mid = (left + right) // 2
    left_half = mergesort(array, left, mid)
    right_half = mergesort(array, mid + 1, right)
    return merge(left_half, right_half)


# O(n) space merging
def merge(a1: list, a2: list):
    array = []
    i, j = 0, 0
    while i < len(a1) or j < len(a2):
        if i < len(a1) and (j >= len(a2) and a1[i] <= a2[j]):
            array.append(a1[i])
            i += 1
        elif j < len(a2):
            array.append(a2[j])
            j += 1
    return array


# O(1) in-place merging
def merge_in_place(array, start, mid, end):
    i, j = start, mid + 1
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            i += 1
        else:
            # Make space for array[j] by shifting elements [i,...,j - 1] to the right
            temp = array[j]
            for k in range(j, i, -1):
                array[k] = array[k - 1]
            array[i] = temp

            i += 1
            mid += 1
            j += 1


# Simple O(nlogn) quicksort
def quicksort(array: list):
    if len(array) <= 1:
        return array
    pivot = random.randint(0, len(array) - 1)
    count = 0

    left_half = []
    right_half = []
    for i in range(len(array)):
        if i == pivot:
            count += 1
        elif array[i] < array[pivot]:
            left_half.append(array[i])
        else:
            right_half.append(array[i])
    return quicksort(left_half) + [array[pivot]] * count + quicksort(right_half)