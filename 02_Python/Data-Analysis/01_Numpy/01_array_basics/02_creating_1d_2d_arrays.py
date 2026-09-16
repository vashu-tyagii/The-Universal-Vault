"""
Topic: Creating 1D and 2D arrays using np.array()

Notes:
- NumPy arrays are created with np.array(iterable).
- A 1D array contains values in a single row-like sequence.
- A 2D array contains rows and columns, so its values are nested lists.
- The shape attribute returns the dimensions as (rows, columns).
- dtype shows the type used to store the values.
"""

import numpy as np


# 1D array: one sequence of values
numbers_1d = np.array([10, 20, 30, 40, 50])
print("1D array:", numbers_1d)
print("1D shape:", numbers_1d.shape)
print("1D dimensions:", numbers_1d.ndim)


# 2D array: rows of values with the same number of columns
numbers_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
print("\n2D array:\n", numbers_2d)
print("2D shape:", numbers_2d.shape)  # 2 rows and 3 columns
print("2D dimensions:", numbers_2d.ndim) # ndim tell type of array, 1D or 2D or 3D etc.


# NumPy infers a common data type for the array.
decimals = np.array([1, 2.5, 3])
print("\nInferred dtype:", decimals.dtype) # dtype is float64 because it can hold all values without losing information.

# A dtype can also be specified explicitly.
integers = np.array([1.2, 2.8, 3.9], dtype=int)
print("Explicit integer dtype:", integers)

# Indexing uses zero-based positions: [row, column] for 2D arrays.
print("\nFirst 1D value:", numbers_1d[0])
print("Value in row 2, column 3:", numbers_2d[1, 2])
