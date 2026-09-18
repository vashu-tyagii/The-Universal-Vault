"""Simple Pandas column operations.

Columns are the named parts of a DataFrame.  We can select, add, rename,
delete, and change columns using simple syntax.
"""

import pandas as pd


# Example DataFrame
students = pd.DataFrame(
	{
		"name": ["Ana", "Ben", "Cara"],
		"math": [90, 75, 88],
		"english": [85, 80, 92],
	}
)


# 1. Select one column.
names = students["name"]

# Select more than one column (use a list of column names).
scores = students[["math", "english"]]

# 2. Add a new column.
students["total"] = students["math"] + students["english"]

# Create a column from a calculation.
students["average"] = students["total"] / 2

# 3. Rename columns.
students = students.rename(columns={"name": "student_name"})

# 4. Change values in a column.
students["average"] = students["average"].round(1)

# 5. Delete a column.
# Use inplace=True to change the existing DataFrame directly.
students.drop(columns="total", inplace=True)

# 6. Change the order of columns.
students = students[["student_name", "math", "english", "average"]]

# 7. Get all column names.
column_names = students.columns

# Display the result when this file is run.
print(students)
print("Column names:", list(column_names))
