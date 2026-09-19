# NumPy + Pandas — Quick Reference Notes

Short "what it does" + minimal syntax for every function/topic covered. 
Use this for revision — not for learning from scratch.

---

# 🔢 NUMPY

## Array Creation

**Array vs List** — NumPy arrays are faster and support element-wise math; 
lists don't.
```python
np.array([1, 2, 3])
```

**1D / 2D Array**
```python
np.array([1, 2, 3])              # 1D
np.array([[1, 2], [3, 4]])       # 2D
```

**Zeros / Ones**
```python
np.zeros(5)          # array of 5 zeros
np.ones((3, 4))      # 3x4 array of ones
```

**Arange** — generate a range of numbers (like range(), but returns an array)
```python
np.arange(0, 20)         # 0 to 19
np.arange(10, 50, 5)     # 10 to 45, step 5
```

**Random Numbers** — generate dummy/test data
```python
np.random.rand(3)            # 3 random floats (0-1)
np.random.randint(1, 100, 5) # 5 random ints between 1-100
```

---

## Array Properties

**Shape / Size / Ndim**
```python
arr.shape   # dimensions, e.g. (2, 3)
arr.size    # total number of elements
arr.ndim    # number of dimensions
```

---

## Indexing & Slicing

**Indexing** — access a single element
```python
arr[0]          # first element
arr[-1]         # last element
arr_2d[1, 2]    # row 1, column 2
```

**Slicing** — extract a range
```python
arr[1:4]        # index 1 to 3
arr_2d[1]       # entire row 1
arr_2d[:, 0]    # entire first column
```

**Boolean Indexing** — filter by condition (heavily used later in Pandas)
```python
arr[arr > 15]   # only values greater than 15
```

**Comparison Operations** — returns True/False array
```python
arr > 15
```

---

## Operations

**Element-wise Math**
```python
arr + 10
arr * 3
arr1 + arr2
```

**Reshaping**
```python
arr.reshape(2, 3)   # reshape into 2 rows, 3 columns
```

**Concatenation / Stacking**
```python
np.concatenate([arr1, arr2])
np.vstack([arr1, arr2])   # stack vertically
np.hstack([arr1, arr2])   # stack horizontally
```

---

## Aggregation

**Aggregate Functions**
```python
arr.sum()
arr.mean()
arr.min()
arr.max()
arr.std()
```

**Axis** — direction of calculation in 2D arrays
```python
arr_2d.sum(axis=0)   # column-wise
arr_2d.sum(axis=1)   # row-wise
```

---

# 🐼 PANDAS

## Creating Data

**Series** — 1D labeled array
```python
pd.Series([10, 20, 30], index=["a", "b", "c"])
```

**DataFrame** — 2D labeled table
```python
pd.DataFrame({"name": ["A", "B"], "marks": [80, 90]})
```

---

## Reading & Exploring Data

**Read CSV / Excel**
```python
pd.read_csv("file.csv")
pd.read_excel("file.xlsx")
```

**Explore a DataFrame**
```python
df.head()        # first 5 rows
df.tail()        # last 5 rows
df.info()        # column types, nulls, memory
df.describe()    # summary stats (numeric columns)
df.shape         # (rows, columns)
df.columns       # list of column names
```

---

## Selecting & Filtering

**Select a column**
```python
df["column_name"]
df.column_name
```

**loc vs iloc**
```python
df.loc["label"]      # select by label
df.iloc[0]            # select by position (index number)
```

**Filter rows by condition**
```python
df[df["marks"] > 50]
df[(df["marks"] > 50) & (df["city"] == "Delhi")]   # multiple conditions
```

---

## Column Operations

**Create a new column**
```python
df["new_col"] = df["marks"] * 2
```

**Rename a column**
```python
df.rename(columns={"old_name": "new_name"}, inplace=True)
```

**Drop a column**
```python
df.drop("col_name", axis=1, inplace=True)
```

**Sort data**
```python
df.sort_values("marks", ascending=False)
```

---

## Cleaning Data

**Check missing values**
```python
df.isna()             # True/False table
df.isna().sum()        # count of nulls per column
```

**Handle missing values**
```python
df.dropna()                    # remove rows with any null
df.fillna(0)                   # fill nulls with a value
```

**Find duplicates**
```python
df.duplicated()                     # True/False per row
df["col"].duplicated().sum()        # count of duplicate values
df[df.duplicated()]                 # show duplicate rows
df.drop_duplicates()                # remove duplicate rows
```

---

## Combining Data

**Merge (like SQL JOIN)**
```python
pd.merge(df1, df2, on="id", how="inner")   # inner/left/right/outer
```

**Concat** — stack DataFrames together
```python
pd.concat([df1, df2], ignore_index=True)
```

**Insert a new row**
```python
df.loc[len(df)] = ["value1", "value2", "value3"]
# or
df = pd.concat([df, new_row_df], ignore_index=True)
```

---

## GroupBy & Aggregation

**GroupBy**
```python
df.groupby("course")["marks"].mean()
df.groupby("course").agg({"marks": "mean", "fees": "sum"})
```

**Pivot Table**
```python
df.pivot_table(index="course", columns="city", values="fees", aggfunc="sum")
```

---

## Exporting Data

**Save to file**
```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```

---

## Common Gotchas (Worth Remembering)

- `df[boolean_condition]` filters the **whole DataFrame** (all columns), not 
  just the column you wrote the condition on.
- `.count()` counts non-null values (per column) — it's not a duplicate 
  counter. Use `.sum()` on a boolean Series to count `True` values.
- `np.arange(start, stop)` — `stop` is always **exclusive**.
- `axis=0` = column-wise (down), `axis=1` = row-wise (across).
