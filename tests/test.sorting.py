from algorithms import mergesort, quicksort, quickselect, kth_smallest, kth_largest

# Test array
array = [3, 5, 1, 2, 5, 8, 34, 1, 12, 19, 45, 1, 0, -12, 1]
array_length = len(array)

print("Mergesort:", mergesort(array.copy()))
print("Quicksort:", quicksort(array.copy()))

# Test kth_smallest and kth_largest using Quickselect
print("\nTesting 1-indexed kth smallest and kth largest elements:")
for i in range(1, array_length + 1):
    kth_smallest_element = kth_smallest(array.copy(), i)
    kth_largest_element = kth_largest(array.copy(), i)
    print(f"{i}th smallest element: {kth_smallest_element}, {i}th largest element: {kth_largest_element}")
