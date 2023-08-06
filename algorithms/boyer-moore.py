def boyer_moore(a: list):
    """Returns the majority element from a list"""
    curr_majority = None
    counter = 0

    for element in a:
        if counter == 0:
            curr_majority = element

        if element == curr_majority:
            counter += 1
        else:
            counter -= 1

    instances = 0
    for element in a:
        if element == curr_majority:
            instances += 1
        if instances > len(a) // 2:
            return curr_majority
    return None

# a = [1, 3, 1, 1, 3, 3, 1, 3, 3]  # length 9
