"""Pandas Session 3: Joins, Merge, and Concat Practice Template"""
import pandas as pd
import numpy as np  # type: ignore

# Sample DataFrames for practice
df_students = pd.DataFrame({
    "roll_no": [1, 2, 3, 4],
    "name": ["Vashu", "Shorya", "Aman", "Rohan"]
})

df_scores = pd.DataFrame({
    "roll_no": [2, 3, 4, 5],
    "marks": [85, 90, 78, 92]
})

df_jan = pd.DataFrame({"item": ["Pen", "Book"], "sales": [100, 200]})
df_feb = pd.DataFrame({"item": ["Bag", "Pencil"], "sales": [150, 50]})

df_col1 = pd.DataFrame({"id": [1, 2], "name": ["Vashu", "Shorya"]})
df_col2 = pd.DataFrame({"salary": [50000, 60000]})

print("DataFrames ready for practice!\n")

# 1. Inner Merge: Merge df_students and df_scores using 'roll_no' with how="inner".
# Code here:


# 2. Left Merge: Perform a left merge on df_students and df_scores using 'roll_no' so no student is lost.
# Code here:


# 3. Row-wise Concat: Concatenate df_jan and df_feb vertically (axis=0) and use ignore_index=True.
# Code here:


# 4. Column-wise Concat: Concatenate df_col1 and df_col2 horizontally using axis=1.
# Code here:


# 5. Index-Based Join: Set index of df_students and df_scores to 'roll_no' and use .join() to combine them.
# Code here:
