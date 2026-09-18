"""Handling null values in Pandas.

Null values mean that some data is missing. Pandas usually represents them
as NaN (Not a Number) or None.
"""

import pandas as pd


# Example data with missing values.
data = {  # type: ignore
    "name": ["Ana", "Ben", "Cara", "Dan"],
    "age": [20, None, 25, 30],
    "city": ["London", "Paris", None, "Rome"],
}

df = pd.DataFrame(data)  # type: ignore

# Check which values are missing.
print("Find Nulls:\n")
print(df.isna())

# Count missing values in each column.
print("Missing values per column:")
print(df.isna().sum())

# Show only rows that contain at least one missing value.
print("Rows with missing values:")
print(df[df.isna().any(axis=1)])

# Remove rows with missing values.

without_nulls = df.dropna()
print("DataFrame without null values:")
print(without_nulls)

# Fill missing values with a simple replacement.
print("Copy For Remove Nulls :\n")
filled = df.copy()
filled["age"] = filled["age"].fillna(0).astype(int)
filled["city"] = filled["city"].fillna("Unknown")
print("\nAfter Filed :\n")
print(filled)

# Fill a numeric null with the column average.
average_age = df["age"].mean()
df["age"] = df["age"].fillna(average_age)

# Fill text nulls with the most common value (the mode).
most_common_city = df["city"].mode()[0]
df["city"] = df["city"].fillna(most_common_city)

print("\nAfter Filling Age and City DataFrame:\n", df)


# Quick guide:
# - isna()      finds missing values.
# - dropna()    removes rows or columns with missing values.
# - fillna()    replaces missing values.
# Always use a copy when you want to keep the original DataFrame unchanged.
