"""Pandas: exploring a DataFrame.

Data exploration is the first step after loading data.  These methods help
understand the shape, types, missing values, and basic statistics of a table.
"""

import pandas as pd  # type: ignore


# A small example DataFrame. In practice, this could come from:
# df = pd.read_csv("data.csv")
df = pd.DataFrame(
	{
		"name": ["Alice", "Bob", "Cara", "Dan"],
		"age": [25, 31, 28, 31],
		"department": ["IT", "Sales", "IT", "Sales"],
		"salary": [60000, 72000, 65000, None],
	}
)


# ----- Inspect the structure -----
print('DataFrame Head:\n')
print(df.head())          # First five rows
print("DataFrame Tail:\n") # skip the first few rows and show the last few rows
print(df.tail(2))         # Last two rows
print("DataFrame Shape :\n") # Array type of (number_of_rows, number_of_columns) Column Types and Index 
print(df.shape)           # (number_of_rows, number_of_columns)

print("DataFrame Columns:\n")
print(df.columns.tolist())
print("DataFrame Index:\n")
print(df.index)
print("DataFrame Data Types:\n")
print(df.dtypes)           # Data type of every column
print("DataFrame Info:\n")
print(df.info())           # Types, non-null counts, and memory usage


# ----- Summaries the data -----
print("DataFrame Describe: Give Statistical Summary\n")
print(df.describe())                    # type: ignore # Numeric summary statistics
print("DataFrame Describe: Give Information & Count \n")
print(df.describe(include="str"))    # type: ignore # Summary for text columns
print("DataFrame Value Count \n")
print(df["department"].value_counts())  # Frequency of each category
print("DataFrame Unique Values:\n")
print(df["department"].unique().tolist()) # type: ignore # Categories in a column and their order of appearance
print("DataFrame Number of Unique Values:\n")
print(df["department"].nunique()) # Give the number of unique values in a column Filtering 
# and selecting data is a common task in data analysis.
# Pandas provides several methods to select rows and columns based on conditions, labels, or positions.



# ----- Find and handle missing values -----
print("DataFrame Missing Values: Count\n")
print(df.isna().sum())       # Missing values per column

print("DataFrame Missing Values: True/False\n")
print(df.isna().any())       # type: ignore # Whether each column contains missing data

# Fill missing salary with the column median; alternatives include dropna().
print("DataFrame Fill Missing Values with Median:\n")
df["salary"] = df["salary"].fillna(df["salary"].median()) # type: ignore
# After filling, check for missing values again.
print("DataFrame Missing Values After Fill:\n")
print(df.isna().sum())       # Missing values per column

# ----- Select and filter rows -----
print("DataFrame Select and Filter Rows:\n")
print(df["name"])   # Select one column (Series)
print("\n")
print(df[["name", "salary"]])
print("\n")# Select multiple columns (DataFrame)
print(df.loc[0])                          # Select one row by label (Series)
print("\n")
print(df.loc[1:3, ["name", "salary"]])    # Select multiple rows and columns by label (DataFrame)
print("\n")
print(df.iloc[0])                         # Select one row by position (Series)
print("\n")
print(df.iloc[0:2, 0:3])                  # Select multiple rows and columns by position (DataFrame)
# Pandas provides several methods to select rows and columns based on conditions, labels, or positions.
print("DataFrame Filter Rows by Condition:\n")
print(df.loc[df["age"] > 28, ["name", "age"]]) # type: ignore
print("DataFrame Query Rows:\n")
print(df.query("department == 'IT' and salary >= 60000"))


# ----- Sort and group data -----
print("Sorting Salary in DESC:\n")
print(df.sort_values("salary", ascending=False)) # type: ignore

department_summary = (
	df.groupby("department", as_index=False).agg(average_salary=("salary", "mean"), employee_count=("name", "count"))
)
print("Department Summary :\n")
print(department_summary)


# ----- Useful checks -----
print("Duplicates Value:\n")
print(df)
print(df.duplicated().sum())  # Number of duplicate rows
print("Average Salary:\n")
print(df["salary"].mean())

# Tip: avoid changing the original data accidentally; use .copy() when needed.
it_employees = df.loc[df["department"].eq("IT")].copy() # type: ignore
print(it_employees)
