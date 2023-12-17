# The kth order statistic of a list of numbers is the (1-indexed) kth smallest element.
import heapq
from algorithms import hoare_partition, lomuto_partition


def kth_smallest(array: list, kth: int):
    """
    The kth smallest element is the (x = n - k + 1)th largest.
    O(n + nlogx) worst case complexity
    """
    n = len(array)
    return kth_largest(array, n - kth + 1)

def kth_largest(array: list, kth: int):
    """
    Find the kth smallest element by creating a min-heap and
    popping the minimum element when the heap exceeds size k
    (because then k elements are larger.)

    Continue until the heap has exactly size k and has popped
    all but the largest k elements. the kth largest is now the
    minimum of them.

    O(n + nlogk) worst case complexity
    """
    heap = []

    for num in array:
        heapq.heappush(heap, num)
        if len(heap) > kth:
            heapq.heappop(heap)
    return heap[0]

# faster than minheap approach on average
def quickselect(array, kth: int):
    """
    Partition the array and determine which subarray to recurse in
    to find the kth smallest element. O(n) worst case (using medians)
    """

    """
    Partition the array with Lomuto s.t. the integer at the pivot
    index is in its final sorted location. Then, array[pivot] is
    the (pivot-index + 1)th smallest integer.
    """
    def qs_lomuto(left: int, right: int):
        pivot_index = lomuto_partition(array, left, right)
        if kth == pivot_index + 1: # account for 1-indexed
            return array[pivot_index] # guaranteed to terminate
        elif kth < pivot_index + 1:
            return qs_lomuto(left, pivot_index - 1)
        else:
            return qs_lomuto(pivot_index + 1, right)

    """
    Partition the array with Hoare and determine if kth is in the
    left inclusive subarray (which contains the [1 to left_size + 1)
    smallest integers of [left, right]) or else to the right.
    """
    def qs_hoare(left: int, right: int, kth: int = kth):
        if left == right: # k is the smallest of 1
            return array[left]

        pivot_index = hoare_partition(array, left, right)
        left_size = pivot_index - left + 1
        if kth < left_size + 1: # account for 1-indexed
            return qs_hoare(left, pivot_index, kth)
        else: # take out the (left_size) smaller numbers than k
            return qs_hoare(pivot_index + 1, right, kth - left_size)

    if kth <= 0 or kth > len(array):
        return "k out of bounds"
    return qs_hoare(0, len(array) - 1)
