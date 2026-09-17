"""
Topic: Comparison operations on NumPy arrays

Comparison operators are applied element by element and return a Boolean
array (a mask). The mask can be used for filtering or selecting values.

Common operators:
	==   equal to
	!=   not equal to
	>    greater than
	>=   greater than or equal to
	<    less than
	<=   less than or equal to

Use `&` (and), `|` (or), and `~` (not) for array conditions. Put each
condition in parentheses; Python's `and` and `or` do not work with arrays.
"""

import numpy as np


# A comparison is performed independently for every element.
arr = np.array([2, 5, 8, 11, 14])
greater_than_five = arr > 5
print(greater_than_five)  # [False False  True  True  True]

# Other comparison operators
print(arr == 8)   # [False False  True False False]
print(arr != 8)   # [ True  True False  True  True]
print(arr <= 8)   # [ True  True  True False False]

# Boolean masks filter an array and can also be used to replace values.
print(arr[arr > 5])  # [ 8 11 14]
arr[arr < 6] = 0
print(arr)  # [ 0  0  8 11 14]

# Combine conditions with bitwise operators.
values = np.array([3, 7, 10, 15, 20])
between_five_and_fifteen = (values >= 5) & (values <= 15)
print(values[between_five_and_fifteen])  # [ 7 10 15]

is_small_or_large = (values < 5) | (values > 15)
print(values[is_small_or_large])  # [ 3 20]

# `np.any` and `np.all` reduce a Boolean array to one Boolean value.
print(np.any(values > 18))  # True
print(np.all(values != 0))  # True
