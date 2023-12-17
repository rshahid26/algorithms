# The kth order statistic of a list of numbers is the (1-indexed) kth smallest element.
import heapq
from .partition import hoare_partition, lomuto_partition


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
    to find the kth smallest element.

    T(n) = T(n/2) + O(n) = O(n) worst case (requires MM)
    """

    """
    Partition the array with Lomuto s.t. the integer at the pivot
    index is in its final sorted location. Then, array[pivot] is
    the (pivot-index + 1)th smallest integer.
    """
    def qs_lomuto(left: int, right: int):
        pivot_index = lomuto_partition(array, left, right)
        if kth == pivot_index + 1: # account for 1-indexed
            return array[pivot_index]
        elif kth < pivot_index + 1:
            return qs_lomuto(left, pivot_index - 1)
        else:
            return qs_lomuto(pivot_index + 1, right)

    """
    Partition the array with Hoare s.t.
    """
    def qs_hoare(left: int, right: int, kth: int):
        if left == right:
            return array[left]

        pivot_index = hoare_partition(array, left, right)
        num_left = pivot_index - left + 1
        if kth <= num_left:
            return qs_hoare(left, pivot_index, kth)
        else:
            return qs_hoare(pivot_index + 1, right, kth - num_left)

    def qs_MM(left: int, right: int):
        pass

    if kth <= 0 or kth > len(array):
        return "k out of bounds"
    return qs_hoare(0, len(array) - 1, kth)

