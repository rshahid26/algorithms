import math


def binary_search(list, target):
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

