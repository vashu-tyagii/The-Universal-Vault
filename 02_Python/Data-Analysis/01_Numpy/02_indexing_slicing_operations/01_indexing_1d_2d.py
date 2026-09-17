"""
Topic: Indexing arrays — accessing single elements in 1D and 2D arrays

Notes:
		* NumPy uses zero-based indexing: the first item is at index 0.
		* 1D arrays use array[index]. Negative indices count from the end.
		* 2D arrays use array[row, column]. The first index is the row and the
			second index is the column.
		* Indexing one element returns a scalar; selecting a row or column returns
			an array.
"""

import numpy as np


# 1D indexing
numbers = np.array([10, 20, 30, 40, 50])

print("1D array:", numbers)
print("First element:", numbers[0])   # 10
print("Third element:", numbers[2])   # 30
print("Last element:", numbers[-1])   # 50


# 2D indexing: array[row, column]
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print("\n2D array:\n", matrix)
print("Top-left element:", matrix[0, 0])       # 1
print("Middle element:", matrix[1, 1])         # 5
print("Bottom-right element:", matrix[-1, -1])  # 9
print("Second row:", matrix[1])                # [4 5 6]
print("Third column:", matrix[:, 2])           # [3 6 9]
