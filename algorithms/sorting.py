import random
from .partition import hoare_partition

# Forward traversal
def selection_sort(array: list):
    """
    Sorts in O(n^2) worst case. Iterates forwards from j in [i, end)
    and identifies the smallest element in this subarray. Then it swaps
    it with the element at index i and continues.
    """
    for i in range(len(array)):
        min_index = i

        for j in range(i, len(array), 1):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


def insertion_sort(array: list):
    """
    Sorts in O(n^2) worst case. Iterates backwards from j in [0, i)
    and shifts elements to j + 1 until the elements are smaller than
    array[i]. Then, it inserts array[i] into the new hole.

    Like selection sort, after i passes though the array, the first
    i elements are in sorted order. However, unlike selection sort,
    these elements are not the i smallest elements (yet).
    """
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1

        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp
    return array


def mergesort(array: list, left: int = None, right: int = None):
    """
    Sorts an array by repeatedly dividing it in half until it is
    composed of n subarrays of size 1. Then, it repeatedly combines them
    into n/2 sorted subarrays in O((2^k)n/(2^k)) = O(n) time.

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
        if j >= len(a2) or (i < len(a1) and a1[i] <= a2[j]):
            array.append(a1[i])
            i += 1
        else:
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


# O(1) space
def quicksort(array: list, left: int = None, right: int = None):
    """
    Sorts an array by partitioning its elements into two subarrays,
    one of elements < some pivot and one of elements > pivot. These
    subarrays can now be sorted individually.

    T(n) = 2T(ceil((n-1)/2)) + O(n) = O(nlogn) best case
    T(n) = T(n - 1) + O(n) = O(n^2) worst case
    """
    if left is None or right is None:
        left, right = 0, len(array) - 1

    if left < right:
        pivot_index = hoare_partition(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)
    return array



def naive_quicksort(array: list):
    if len(array) <= 1:
        return array

    # O(n) space partition scheme
    pivot, count = array[random.randint(0, len(array) - 1)], 1
    left_half, right_half = [], []
    for num in array:
        if num == pivot:
            count += 1
        elif num < pivot:
            left_half.append(num)
        else:
            right_half.append(num)

    return naive_quicksort(left_half) + [pivot] * count + naive_quicksort(right_half)
