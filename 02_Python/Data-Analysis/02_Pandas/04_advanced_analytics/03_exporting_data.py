"""Exporting data with pandas.

The examples below use small data sets so the main ideas are easy to see.
"""

import pandas as pd


# Create a small DataFrame to use in the examples.
df = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["London", "Paris", "Tokyo"],
    }
)


# Export to CSV.  index=False prevents pandas from adding row numbers.
df.to_csv("people.csv", index=False)

# Export to Excel when the optional Excel dependency is installed.
try:
    df.to_excel("people.xlsx", index=False)  # pyright: ignore[reportUnknownMemberType]
except ImportError:
    print("Skipping Excel export: install openpyxl to enable it.")

# Export to JSON.  Records format creates one JSON object per row.
df.to_json("people.json", orient="records", indent=4)

# Export only selected columns when a smaller file is needed.
df[["name", "city"]].to_csv("names_and_cities.csv", index=False)

# Read an exported CSV file back into a DataFrame.
loaded_df = pd.read_csv("people.csv")
print(loaded_df)
