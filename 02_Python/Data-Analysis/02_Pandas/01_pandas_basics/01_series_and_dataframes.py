"""Pandas Series and DataFrames: notes and examples.

Series
------
* A Series is a one-dimensional labelled array.
* It contains values and an index (row labels).

DataFrame
---------
* A DataFrame is a two-dimensional table of labelled columns and rows.
* Each column is a Series, and columns may have different data types.
* ``loc`` selects by label; ``iloc`` selects by integer position.
* Pandas aligns values by labels during operations and uses ``NaN``/``pd.NA``
  for missing values.
"""

import numpy as np
import pandas as pd  # type: ignore


# ------------------------------- Series ---------------------------------
# series is a 1d array with an index (row labels)
temperatures = pd.Series(
    np.array([18.5, 21.0, 19.2]),
    index=["Monday", "Tuesday", "Wednesday"],
    name="temperature"
)

print("Series:\n", temperatures)
# loc is use for label-based indexing
print("Tuesday's temperature:", temperatures.loc["Tuesday"])
# iloc is use for position-based indexing
print("First two values:\n", temperatures.iloc[:2])

# ----------------------------- DataFrame --------------------------------
# A DataFrame is a 2d table of labelled columns and rows.
# It can be created from a dictionary of Series or arrays.
weather = pd.DataFrame(
    {
        "day": ["Monday", "Tuesday", "Wednesday"],
        "temperature": np.array([18.5, 21.0, 19.2]),
        "rain": np.array([True, False, False]),
    }
)

print("\nDataFrame:\n", weather)
print("\nShape (rows, columns):", weather.shape)
# ``tolist()``
print("Column names:", weather.columns.tolist())
# Tolist is use to convert the column names to a list
print("\nOne column (returns a Series):\n", weather["temperature"])
# calling a column as an attribute is equivalent to using the bracket notation
print("\nOne column (returns a Series):\n", weather.temperature)
print("\nFirst row:\n", weather.iloc[0])
rows_without_rain = weather.loc[~weather["rain"]]
# The tilde (~) operator negates the boolean Series, so this selects rows where "rain" is False.
# Jess din barish nahi hui, un rows ko select karne ke liye humne tilde (~) operator ka use kiya hai.
print("\nRows without rain:\n", rows_without_rain)
print("Mean temperature without rain:",
      rows_without_rain["temperature"].mean())
# To calculate the mean temperature for days without rain, we first filter the DataFrame
# to include only those rows where "rain" is False. Then, we access the "temperature"
# column of this filtered DataFrame and call the `mean()` method to compute the average temperature.

# Create a derived column and calculate a summary statistic.
weather["fahrenheit"] = weather["temperature"] * 9 / 5 + 32
# Adding a new column "fahrenheit" to the DataFrame by converting the "temperature" column from Celsius to Fahrenheit using the formula F = C * 9/5 + 32.
print("\nAverage temperature:", weather["temperature"].mean())
# The `mean()` method calculates the average of the "temperature" column in the DataFrame.
print("NumPy average temperature:", np.mean(weather["temperature"].to_numpy()))
# The `to_numpy()` method converts the "temperature" column to a NumPy array, and then we use `np.mean()` to calculate the average temperature.
print("\nUpdated DataFrame:\n", weather)


# Reindexing demonstrates label alignment and missing data.
sales = pd.Series({"Monday": 10, "Tuesday": 14, "Wednesday": 12})
sales_by_day = sales.reindex(weather["day"])
print("\nSales with missing Wednesday:\n", sales_by_day)
# Why it add Wednesday as NaN? Because we reindexed the `sales`
# Series to match the index of the `weather["day"]` Series, which includes "Wednesday".
# Since "Wednesday" was not present in the original `sales` Series, it is added with a value of `NaN` to indicate missing data.

print("\nNumeric summary:\n", weather.describe())  # type: ignore
print("\nCategorical summary:\n", weather.describe(include="str"))  # type: ignore
# Useful methods with examples:
print("\nFirst two rows:\n", weather.head(2))

print("\nDataFrame information:")
weather.info()

print("\nMissing values per column:\n", weather.isna().sum())

# Save the DataFrame as a CSV file without writing the index column.
# weather.to_csv("weather.csv", index=False)

data1 = {"Name": ["Aman", "Rahul", "Rahul", None],  # type: ignore
         "Age": [21, None, 22, 22]}  # type: ignore
df = pd.DataFrame(data1)  # type: ignore

# Missing values check karna
print("Boolean check:\n", df.isna())

# Column-wise total missing count
print("\nTotal missing per column:\n", df.isna())

# Find duplicate rows and duplicate values in a column.
# duplicate_rows = df[df.duplicated()]
# print("\nDuplicate rows:\n", duplicate_rows)
print("\nDuplicate names:", df[df["Name"].duplicated()].sum().count())

