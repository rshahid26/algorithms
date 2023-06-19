# Backward traversal
def sort_bf(list):
    """
    Sorts in worst case O(n^2) by iterating through an array
    and bringing the greatest element [j] < i to the front
    with each new element i.
    """
    for i in range(len(list)):
        for j in range(i):

            if list[i] < list[j]:
                list[i], list[j] = list[j], list[i]

    return ''.join(list)


# Forward traversal
def selection_sort(list):
    """
    Sorts all cases in O(n^2) by iterating through an array
    and bringing the least element [j] > i to the back
    with each new element i.
    """
    for i in range(len(list)):
        for j in range(i, len(list), 1):

            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]

    if isinstance(list, str):
        return ''.join(list)
    return list


def insertion_sort(list):
    """
    Sorts in worse case O(n^2) by iterating through an array
    and shifting all greater elements [j] < i to [j+1] until
    the right spot for the element i is found.
    """
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key
    return ''.join(list)


# test_string = "insertionsort"
# print(sort_bf(list(test_string)))
# print(selection_sort(list(test_string)))
