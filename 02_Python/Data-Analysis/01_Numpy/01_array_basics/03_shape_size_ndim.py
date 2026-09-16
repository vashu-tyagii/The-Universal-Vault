"""
Topic: Array shape, size, and dimensions — .shape, .ndim, .size

Notes:
	.shape returns the length of the array along each axis. For a 2-D array,
	the result is (rows, columns).
	.ndim returns the number of dimensions (axes).
	.size returns the total number of elements. It is the product of shape.
"""

import numpy as np


# A 2-D array with 2 rows and 3 columns.
numbers = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(numbers)
print("Shape:", numbers.shape)       # (2, 3)
print("Dimensions:", numbers.ndim)   # 2
print("Size:", numbers.size)         # 6

# The properties also work for arrays with other numbers of dimensions.
one_dimensional = np.array([10, 20, 30, 40])
three_dimensional = np.array([[
    [1, 2],
    [3, 4]
],
    [[5, 6],
     [7, 8]
     ]])
print(three_dimensional)
print("1-D:", one_dimensional.shape, one_dimensional.ndim, one_dimensional.size)
print("3-D:", three_dimensional.shape,
      three_dimensional.ndim, three_dimensional.size)

# For numbers, 2 * 3 = 6, which matches numbers.size.
