from algorithms import quickselect, kth_smallest, kth_largest

# Test array
array = [0, -4, -7, 3, 0, 8, 2]

# Test kth_smallest and kth_largest using Quickselect
print("\nTesting 1-indexed kth smallest and kth largest elements:")
for i in range(1, len(array) + 1):
    kth_smallest_element = kth_smallest(array.copy(), i)
    kth_largest_element = kth_largest(array.copy(), i)
    print(f"{i}th smallest element: {kth_smallest_element}, {i}th largest element: {kth_largest_element}")

print("\nTesting quickselect:")
print(f"{4}th smallest element: {quickselect(array, 4)}")
