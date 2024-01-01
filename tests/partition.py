from computer_science import hoare_partition, lomuto_partition

array = [5, 2, 4, 7, 6, 1, 3]
print(array)
pivot_index = hoare_partition(array)
print(array)
print("element", array[pivot_index], "at index", pivot_index)