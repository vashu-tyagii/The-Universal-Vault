"""
Topic: Array vs List — why NumPy arrays exist, how they differ from Python lists

Key notes
---------
- A Python list is a general-purpose container. It can store values of different
	types, but numeric operations must usually be written with loops or
	comprehensions.
- A NumPy array is designed for numerical data. Its elements normally share one
	data type, and operations are vectorized (applied to all elements at once).
- NumPy arrays use less memory for large, homogeneous numeric data and are often
	much faster for calculations.
- Array arithmetic is element-wise. The ``+`` operator on lists concatenates;
	it does not add corresponding values.
- NumPy arrays are usually fixed-size in shape. Use ``reshape`` when the number
	of elements stays the same, and create a new array when changing size.

Install NumPy if necessary:
		python -m pip install numpy
"""

import numpy as np


# The same data represented by a Python list and a NumPy array.
numbers_list = [1, 2, 3, 4]
numbers_array = np.array(numbers_list)

print("list: ", numbers_list)
print("array:", numbers_array)
print("array type:", numbers_array.dtype)

# Lists concatenate, while arrays perform element-wise arithmetic.
print("list + list:  ", numbers_list + numbers_list)
print("array + array:", numbers_array + numbers_array)
print("array * 2:    ", numbers_array * 2)

# A list equivalent requires an explicit loop or comprehension.
list_doubled = [number * 2 for number in numbers_list]
print("list doubled:", list_doubled)

# Useful array properties and operations.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nshape:", matrix.shape)  # two rows, three columns
print("dimensions:", matrix.ndim)
print("sum:", matrix.sum())
print("column means:", matrix.mean(axis=0))
print("reshaped:\n", matrix.reshape(3, 2))

# Array indexing and boolean filtering.
print("first row:", matrix[0])
print("values greater than 3:", matrix[matrix > 3])

# Arrays generally contain one compatible data type.
mixed_array = np.array([1, 2.5, 3])
print("\ncommon dtype:", mixed_array.dtype)
