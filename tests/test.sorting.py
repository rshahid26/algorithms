from algorithms import mergesort, quicksort, quickselect


array = [3, 5, 1, 2, 5, 8, 34, 1, 12, 19, 45, 1, 0, -12, 1]
print(mergesort(array))
print(quicksort(array))

print()
array = [0, 1, 2, 3, 9, 4, 5, 6, 7, 8]
print(array, "length", len(array))
print(quicksort(array))

for i in range(len(array)):
    print(quickselect(array, i + 1), "is the", i + 1, "th smallest integer (1-indexed)")
