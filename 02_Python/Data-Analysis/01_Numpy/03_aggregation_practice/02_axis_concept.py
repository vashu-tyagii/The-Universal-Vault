"""
Topic: The axis concept — row-wise (axis=1) vs column-wise (axis=0) operations

Notes
-----
For a 2-D NumPy array:

* ``axis=0`` works down the rows, so it aggregates each column.
* ``axis=1`` works across the columns, so it aggregates each row.
* ``axis=None`` aggregates every value in the array and returns one scalar.

Keep this memory aid in mind: the axis being removed is the direction in
which NumPy moves while calculating the result.  Therefore, summing with
``axis=0`` removes the row dimension and leaves one result per column.
"""

import numpy as np


sales = np.array(
	[
		[120, 150, 180],  # January
		[100, 130, 160],  # February
		[140, 170, 200],  # March
	]
)


# Each column's total: the operation moves down the rows.
monthly_totals_by_product = sales.sum(axis=0) # for columns

# Each row's total: the operation moves across the columns.
product_totals_by_month = sales.sum(axis=1)

# Other common aggregations use the same axis rule.
column_averages = sales.mean(axis=0)
row_maximums = sales.max(axis=1)
overall_total = sales.sum(axis=None)

print("Sales:\n", sales)
print("Totals for each column (axis=0):", monthly_totals_by_product)
print("Totals for each row (axis=1):", product_totals_by_month)
print("Average of each column:", column_averages)
print("Maximum of each row:", row_maximums)
print("Overall total (axis=None):", overall_total)
