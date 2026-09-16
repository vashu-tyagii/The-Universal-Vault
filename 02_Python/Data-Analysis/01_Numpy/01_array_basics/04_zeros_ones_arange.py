"""
Topic: np.zeros(), np.ones(), np.arange() — generating arrays without manual input

Notes:
		- np.zeros(shape) creates an array filled with 0.
		- np.ones(shape) creates an array filled with 1.
		- shape can be an integer (one-dimensional) or a tuple (multiple dimensions).
		- np.arange(start, stop, step) creates evenly spaced values. The stop value is
			excluded, just like the second argument in range().
		- Use dtype= to control the data type, for example dtype=int.
"""

import numpy as np


# 1. One-dimensional arrays
zeros = np.zeros(4)
ones = np.ones(4, dtype=int)
numbers = np.arange(1, 6)  # 1, 2, 3, 4, 5; stop (6) is excluded

print("Zeros:", zeros)
print("Ones:", ones)
print("Numbers:", numbers)


# 2. Two-dimensional arrays: shape is (rows, columns)
zero_grid = np.zeros((2, 3), dtype=int)
one_grid = np.ones((2, 3), dtype=int)

print("\nZero grid:\n", zero_grid)
print("One grid:\n", one_grid)


# 3. Choosing a start value and step size
even_numbers = np.arange(0, 11, 2)  # 0, 2, 4, 6, 8, 10
countdown = np.arange(5, 0, -1)     # 5, 4, 3, 2, 1

print("Even numbers:", even_numbers)
print("Countdown:", countdown)


# 4. A common use: create a default array and update selected values
scores = np.zeros(5, dtype=int)
scores[2] = 10
scores[4] = 20
print("Updated scores:", scores)
