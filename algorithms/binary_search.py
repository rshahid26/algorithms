# inclusive bounds
def binary_search(array: list, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# exclusive right bound
def binary_search2(array: list, target):
    left, right = 0, len(array)

    while left < right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid
        else:
            left = mid + 1
    return -1

