"""Simple Pandas sorting notes and examples."""

import pandas as pd


# Sorting arranges rows in a useful order.
data = pd.DataFrame(
	{
		"name": ["Bob", "Alice", "Charlie", "Alice"],
		"age": [25, 30, 20, 30],
		"score": [82, 95, 88, 90],
	}
)

# Sort by one column. Ascending order is the default.
print("Sorted by age:")
print(data.sort_values("age"))

# Use ascending=False for largest-to-smallest order.
print("\nScores from high to low:")
print(data.sort_values("score", ascending=False))

# Sort by multiple columns.
# If two ages are equal, the higher score appears first.
print("\nSorted by age, then score:")
print(data.sort_values(by=["age", "score"], ascending=[True, False]))

# Sort the row labels (the index) with sort_index().
print("\nSorted by index:")
print(data.sort_index())

# Sorting returns a new DataFrame and keeps the original unchanged.
# To change the original DataFrame, use: data.sort_values("name", inplace=True)
