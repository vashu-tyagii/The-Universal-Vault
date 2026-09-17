"""
Topic: Reshaping arrays using .reshape()

Notes:
- ``reshape()`` changes an array's dimensions without changing its data.
- The new shape must contain the same total number of elements.
- Use ``-1`` for one dimension and NumPy will infer its size.
- ``reshape()`` returns a reshaped array; it does not change the original
	array in place.
"""

import numpy as np


# A one-dimensional array with 12 elements.
numbers = np.arange(1, 13)
print("Original:", numbers)
print("Original shape:", numbers.shape)

# Reshape the same data into 3 rows and 4 columns.
matrix = numbers.reshape(3, 4)
print("3 x 4 array:\n", matrix)
print("New shape:", matrix.shape)

# NumPy can infer one dimension when it is written as -1.
inferred_shape = numbers.reshape(2, -1)
# This is equivalent to reshape(2, 6): NumPy calculates 12 / 2 = 6.
explicit_shape = numbers.reshape(2, 6)
print("2 x 6 array using -1:\n", inferred_shape)
print("2 x 6 array using 6:\n", explicit_shape)

# Reshape a multidimensional array back to one dimension.
flattened = matrix.reshape(-1)
print("Flattened:", flattened)

# This would raise ValueError because 5 x 2 does not contain 12 elements:
# invalid = numbers.reshape(5, 2)
