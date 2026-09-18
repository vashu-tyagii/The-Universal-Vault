"""Beginner-friendly notes and examples for pandas pivot tables.

A pivot table groups rows and calculates a useful summary, such as a sum
or an average.
"""

import pandas as pd


# Each row represents one sale.
sales = pd.DataFrame(
	{
		"person": ["Alice", "Bob", "Alice", "Bob", "Cara"],
		"product": ["Book", "Book", "Pen", "Pen", "Book"],
		"amount": [20, 15, 5, 8, 25],
	}
)


# Total sales for each person.
total_by_person = pd.pivot_table(
	sales,
	values="amount",       # Column to calculate
	index="person",        # Group rows by this column
	aggfunc="sum",         # Add the values
)
print("Total sales by person:")
print(total_by_person)


# Total sales for each person and product.
# fill_value=0 changes empty cells to zero.
sales_by_product = pd.pivot_table(
	sales,
	values="amount",
	index="person",
	columns="product",
	aggfunc="sum",
	fill_value=0,
).reset_index()
print("\nSales by person and product:")
print(sales_by_product)


# Calculate more than one summary at the same time.
product_summary = pd.pivot_table(
	sales,
	values="amount",
	index="product",
	aggfunc=["sum", "mean", "count"],
).reset_index()
print("\nProduct summary:")
print(product_summary)


# Common arguments:
# values: the column to calculate
# index: rows used for grouping
# columns: extra groups shown as columns
# aggfunc: calculation, such as "sum", "mean", "count", or "max"
# fill_value: replacement for missing combinations
