"""
Topic: Slicing arrays — extracting ranges/sub-arrays from 1D and 2D arrays

Notes
-----
Array slicing uses the form ``array[start:stop:step]``:

* ``start`` is inclusive; ``stop`` is exclusive.
* Any omitted value uses the default (beginning, end, or step ``1``).
* Negative indexes count from the end, and a negative step reverses an array.
* For a 2D array, use ``array[row_slice, column_slice]``.
* Slices usually return a view of the original array, not an independent copy.
	Use ``.copy()`` when the result must be changed safely.
"""

import numpy as np


# 1D slicing
numbers = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

first_four = numbers[:4]          # [0 1 2 3]
middle = numbers[2:7]             # [2 3 4 5 6]
every_second = numbers[::2]       # [0 2 4 6 8]
last_three = numbers[-3:]         # [7 8 9]
reversed_numbers = numbers[::-1]  # [9 8 7 6 5 4 3 2 1 0]

print("First four:", first_four)
print("Middle:", middle)
print("Every second value:", every_second)
print("Last three:", last_three)
print("Reversed:", reversed_numbers)


# 2D slicing: rows are selected before columns.
matrix = np.arange(1, 13).reshape(3, 4)
print("\nMatrix:\n", matrix)

print("Rows 0-1:\n", matrix[:2, :])       # first two rows, all columns
print("Columns 1-2:\n", matrix[:, 1:3])   # all rows, columns 1 and 2
print("Bottom-right block:\n", matrix[1:, 2:])
print("Every other row/column:\n", matrix[::2, ::2])


# A slice is a view. Changing it can change the original array.
# ``numbers[1:4]`` selects indexes 1, 2, and 3 without copying the data.
# Therefore, assigning through ``view`` also updates those elements in
# ``numbers``.
view = numbers[1:4] 
view[:2] = -1
print("\nAfter changing a slice:", numbers)

# Make an independent array when changes must not affect the source.
safe_copy = numbers[1:4].copy()
safe_copy[:] = 100
print("Original after changing a copy:", numbers)
print("Copy:", safe_copy)
