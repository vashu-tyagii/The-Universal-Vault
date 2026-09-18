"""Pandas Part 1: Exploration, Cleaning, and Manipulation — 10 Practice Template"""
import pandas as pd  # type: ignore

# 1. Create a DataFrame with columns: name, age, department, salary (include one NaN in salary).
# Print its shape and column names list.
df = pd.DataFrame(
    {"Name": ['Vashu Tyagi', 'Shorya Sharma'],
     "Age": [21, 20],
     "Department": ['IT', 'SALES'],
     "Salary": [30000, None]
     }
)

# 2. Print the first 3 rows and last 2 rows of the DataFrame.
print("\nFirst Three Rows:\n")
print(df.iloc[:3])
print("Last Two Rows:\n")
print(df.iloc[-2:])

# 3. Use describe() to get statistical summary for numeric and text columns.
print("\nDataFrame Statistical Analysis:\n")
print(f"Use describe():\n{df.describe(include='all')}")

# 4. Check the number of missing values in each column using isna().sum().
print("\nChecking Missing Values:\n ")
print(f"Missing Values: \n{df.isna().sum()}")

# 5. Fill missing values in the 'salary' column with the median salary.
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
print(f"\nAfter Fill Value : \n{df}")
# 6. Select 'name' and 'salary' columns, and print rows where age > 28 using loc.
print(f"\nFiltering Values :\n {df.loc[df['Age'] > 20]}")

# 7. Use the query method to filter employees in 'IT' department with salary >= 60000.
print("\nUsing Query: \n", df.query("Department == 'IT' and Salary >= 60000"))

# 8. Sort the DataFrame by salary in descending order.
print(f"\nSalary in DESC : \n{df.sort_values('Salary', ascending=False)}")

# 9. Group by department to find the average salary and employee count using agg().
print(
    f"\nDepartment wise Avg salary: \n{df.groupby('Department').agg(avg_salary=('Salary', 'mean'), emp_count=('Name', 'count'))}")

# 10. Filter IT employees into a new DataFrame using .copy() to avoid SettingWithCopyWarning.
it_employees = df.loc[df["Department"] == "IT"].copy()
print(f"\nIT Employees:\n{it_employees}")
