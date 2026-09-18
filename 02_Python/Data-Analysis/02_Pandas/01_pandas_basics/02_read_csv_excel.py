"""Pandas: reading and writing CSV and Excel files.

Notes:
    * ``read_csv`` reads comma-separated data; use ``sep`` for another delimiter.
    * ``read_excel`` reads an Excel sheet; install ``openpyxl`` for ``.xlsx`` files.
    * ``usecols`` selects columns, ``nrows`` limits rows, and ``parse_dates`` parses dates.
    * ``head()``, ``info()``, and ``describe()`` are useful for inspecting imported data.
    * ``index=False`` prevents pandas from writing the DataFrame index as a column.
"""

# StringIO lets us treat the text below like a file, so this example does not
# need an external CSV file.
from io import StringIO

# Import pandas with the conventional short name ``pd``.
import pandas as pd


# CSV example: each row contains a date, product, quantity, and unit price.
# In a real project, replace StringIO(csv_data) with a file path such as
# pd.read_csv("data/sales.csv").
csv_data = """date,product,units,price
2024-01-01,Notebook, 3,  5.50
2024-01-02,Pen,      10, 1.25
2024-01-03,Notebook, 2,  5.50
"""

sales = pd.read_csv(
    StringIO(csv_data),
    parse_dates=["date"],  # Convert the date column from text to datetime.
    na_values=["NA", "missing"],  # Treat these values as missing data.
)

# Display the first five rows to quickly verify that the file was read.
print("Sales Head:\n")
print(sales.head())
# Show column names, data types, and the number of non-missing values.

print("Sales Info:\n")
sales.info()
# Provide summary statistics for numeric columns such as units and price.
print("\nSales Describe:\n")
print(sales.describe())  # type: ignore

# Create a calculated column: revenue = number of units multiplied by unit price.
sales["revenue"] = sales["units"] * sales["price"]
# Sum the revenue column to calculate total sales revenue.
print("Total revenue:", sales["revenue"].sum())

print("\nSales DataFrame:\n")
print(sales)

# Common CSV options:
# sep changes the delimiter when reading files such as tab-separated data.
tsv_data = "product\tunits\nPen\t3\nNotebook\t10\n"
# it mean s that the data is separated by tab character instead of comma.
tsv_sales = pd.read_csv(StringIO(tsv_data), sep="\t")
print("\nTSV data:\n", tsv_sales)
# usecols loads only the required columns, reducing memory usage.
selected_columns = pd.read_csv(
    StringIO(csv_data),
    usecols=["date", "product"],
    parse_dates=["date"],
)
print("\nSelected columns:\n", selected_columns)
# nrows reads only the first specified number of rows.
first_row = pd.read_csv(StringIO(csv_data), nrows=1)
print("\nFirst row:\n", first_row)


# Excel examples (requires: python -m pip install openpyxl):
# Read one named worksheet from an Excel workbook.
# workbook = pd.read_excel("data/sales.xlsx", sheet_name="Sales")
# Read every worksheet into a dictionary of DataFrames.
# all_sheets = pd.read_excel("data/sales.xlsx", sheet_name=None)
# Write a DataFrame to Excel without adding the DataFrame index as a column.
# workbook.to_excel("output/sales.xlsx", index=False)

# Export the processed DataFrame to CSV. ``index=False`` avoids an extra index
# column in the output file.
# sales.to_csv("output/sales.csv", index=False)
