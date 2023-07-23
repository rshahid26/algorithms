import math

def binary_search(list, target):
    """
    Searches for an element in a sorted array in O(log n) time.
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = math.floor((low + high) / 2)

        if target == list[mid]:
            return mid

        if target < list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# Knuth-Morris-Pratt algorithm for pattern matching strings in O(n) vs O(nm) time.
# noinspection PyPep8Naming
def kmp_search(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = compute_prefix_function(pattern)
    i = j = 0

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            print(f"Found pattern at index {str(i-j)}")
            j = lps[j-1]

        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def compute_prefix_function(pattern):
    length = 0
    prefix_table = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_table[length-1]
            else:
                prefix_table[i] = 0
                i += 1
    return prefix_table
