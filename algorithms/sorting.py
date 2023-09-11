import math
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
    if left is None or right is None:
        left, right = 0, len(array) - 1

    if left == right:
        return [array[left]]
    mid = (left + right) // 2

    left_half = mergesort(array, left, mid)
    right_half = mergesort(array, mid + 1, right)
    return merge(left_half, right_half)


def merge(a1: list, a2: list):
    array = []
    i, j = 0, 0
    while i < len(a1) or j < len(a2):
        if i < len(a1) and j >= len(a2) or i < len(a1) and a1[i] <= a2[j]:
            array.append(a1[i])
            i += 1
        else:
            array.append(a2[j])
            j += 1
    return array


# Simple O(nlogn) quicksort
def quicksort(array: list):
    if len(array) <= 1:
        return array

    pivot = random.randint(0, len(array) - 1)
    left_half = []
    right_half = []

    for i in range(len(array)):
        if i != pivot:
            if array[i] < array[pivot]:
                left_half.append(array[i])
            else:
                right_half.append(array[i])

    return quicksort(left_half) + [array[pivot]] + quicksort(right_half)


array = [3, 5, 1, 2, 5, 8]
print(quicksort(array))

# test_string = "insertionsort"
# print(sort_bf(array(test_string)))
# print(selection_sort(array(test_string)))
