"""
Topic: Element-wise math operations — +, -, *, / applied across whole arrays

Element-wise operations apply calculations to values at matching positions.
Arrays with the same shape can be combined directly; scalar values are
broadcast to every element.

Common operations:
	+   addition
	-   subtraction
	*   multiplication
	/   division (returns floats)
	**  exponentiation

Array shapes must be compatible for broadcasting, and division by zero should
be avoided.
"""

import numpy as np


# Arrays with the same shape: matching indexes are combined.
prices = np.array([10, 20, 30])
discounts = np.array([1, 2, 3])

print(prices + discounts)  # [11 22 33]
print(prices - discounts)  # [ 9 18 27]
print(prices * discounts)  # [10 40 90]
print(prices / discounts)  # [10. 10. 10.]

# A scalar is applied to every element.
print(prices + 5)           # [15 25 35]
print(prices * 2)           # [20 40 60]
print(prices ** 2)          # [100 400 900]

# Practical example: calculate prices after a 10% discount.
discount_rate = 0.10
sale_prices = prices * (1 - discount_rate)
print(sale_prices)          # [ 9. 18. 27.]
