"""Simple notes and examples for combining pandas DataFrames.

Merge = match rows using a shared column.
Join  = match rows using the index.
Concat = stack DataFrames together.
"""

import pandas as pd


# Two small tables with one shared column: customer_id.
customers = pd.DataFrame(
	{
		"customer_id": [1, 2, 3],
		"name": ["Ana", "Ben", "Cara"],
	}
)

orders = pd.DataFrame(
	{
		"customer_id": [1, 1, 2, 4],
		"item": ["Book", "Pen", "Bag", "Pencil"],
	}
)


# INNER merge: keep only matching customer IDs.
inner_merge = pd.merge(customers, orders, on="customer_id", how="inner")

# LEFT merge: keep every customer, even if they have no order.
left_merge = pd.merge(customers, orders, on="customer_id", how="left")

# RIGHT merge: keep every order, even if the customer is not in the customer table.
right_merge = pd.merge(customers, orders, on="customer_id", how="right")

# OUTER merge: keep all IDs from both tables.
outer_merge = pd.merge(customers, orders, on="customer_id", how="outer")


# A join matches rows by index instead of a named column.
customer_names = customers.set_index("customer_id")[["name"]]
order_items = orders.set_index("customer_id")[["item"]]
index_join = customer_names.join(order_items, how="left")


# Concat stacks rows (axis=0) or adds columns (axis=1).
first_orders = orders.iloc[:2]
last_orders = orders.iloc[2:]
rows_stacked = pd.concat([first_orders, last_orders], ignore_index=True)


if __name__ == "__main__":
	print("INNER MERGE")
	print(inner_merge)

	print("\nLEFT MERGE")
	print(left_merge)

	print("\nINDEX JOIN")
	print(index_join)

	print("\nSTACKED ROWS")
	print(rows_stacked)
