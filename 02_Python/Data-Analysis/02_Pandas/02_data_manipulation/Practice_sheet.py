"""Pandas Part 2: Data Manipulation Practice Template"""
import pandas as pd
import numpy as np  # type: ignore

# Sample DataFrame for practice
df = pd.DataFrame({
    "Name": ["Vashu", "Shorya", "Aman", "Rohan"],
    "Department": ["IT", "SALES", "IT", "HR"],
    "Salary": [65000, 45000, 72000, 50000],
    "Price": [100, 200, 150, 300],
    "Quantity": [5, 2, 4, 3],
    # Note: Age is string here for astype practice
    "Age": ["21", "22", "24", "23"]
})

print("Original DataFrame:\n", df)

# 1. Multiple Conditions Filtering: Filter rows where Department is 'IT' AND Salary > 60000 using '&'.
# Code here:
df_1 = df[(df['Department'] == 'IT') & (df['Salary'] > 60000)]
print(f"\nMultiple Conditions Filtering: \n{df_1}")

# 2. Feature Engineering (New Column): Create 'Total_Revenue' by multiplying 'Price' and 'Quantity'.
# Code here:

df['Total_Revenue'] = df['Price'] * df['Quantity']
print("\nAfter Adding New Column DataFrame:\n", df)

# 3. Data Type Casting: Convert the 'Age' column from string to integer using astype().
# Code here:
df['Age'] = df['Age'].astype(int)
print("After Change DataType DataFrame:\n", df)

# 4. String Operations: Convert all names in the 'Name' column to lowercase using the .str accessor.
# Code here:
df['Name'] = df['Name'].str.lower()
print("After Change name to lower DataFrame:\n", df)


# 5. Dropping Columns: Drop the 'Price' column permanently from the DataFrame using drop().
# Code here:

df.drop(columns='Price', inplace=True)

print("After Drop a Column  DataFrame:\n", df)
