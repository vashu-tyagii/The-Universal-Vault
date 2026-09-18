"""Simple notes and examples for pandas groupby and aggregation.

groupby() lets us split data into groups, calculate something for each group,
and then combine the results into a new table.
"""

import pandas as pd


# Example data: sales made by different people in different departments.
sales = pd.DataFrame(
	{
		"department": ["Books", "Books", "Games", "Games", "Music"],
		"employee": ["Ana", "Ben", "Ana", "Cara", "Ben"],
		"amount": [20, 35, 50, 40, 25],
		"items": [2, 3, 5, 4, 2],
	}
)


# Group by one column and calculate the total amount for each department.
total_by_department = sales.groupby("department")["amount"].sum()
print("Total sales by department:")
print(total_by_department)


# Other common calculations include mean(), count(), min(), and max().
average_by_department = sales.groupby("department")["amount"].mean()
print("\nAverage sale by department:")
print(average_by_department)


# Group by more than one column.
total_by_department_and_employee = (
	sales.groupby(["department", "employee"])["amount"].sum()
)
print("\nTotal sales by department and employee:")
print(total_by_department_and_employee)


# agg() applies several calculations at the same time.
summary = sales.groupby("department").agg(
	total_amount=("amount", "sum"),
	average_amount=("amount", "mean"),
	total_items=("items", "sum"),
)
print("\nDepartment summary:")
print(summary)


# Use reset_index() when you want group names to become normal columns.
summary_as_columns = summary.reset_index()
print("\nSummary with department as a column:")
print(summary_as_columns)


# Notes:
# - groupby("column") creates groups using the values in that column.
# - Select a column before a calculation: ["amount"].sum().
# - Use agg() for multiple calculations or for calculations on different columns.
# - reset_index() changes the grouped index back into a regular column.
