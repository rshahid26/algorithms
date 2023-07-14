def deleteProducts(ids, m):
    instances = {}
    array = [0] * len(ids)
    counter = 0

    for id in ids:
        if id in instances:
            array[instances[id]] += 1
        else:
            instances[id] = counter
            array[instances[id]] = 1
            counter += 1
    array.sort()
    print(array)

    for index in range(len(array)):
        m = m - array[index]
        if m == 0:
            return len(array) - (index + 1)
        if m < 0:
            return len(array) - index
    return 0


print(deleteProducts([], 6))
