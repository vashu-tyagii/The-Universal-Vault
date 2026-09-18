"""Filtering rows in a pandas DataFrame.

Filtering means selecting only the rows that match a condition.
"""

import pandas as pd


# Example data
students = pd.DataFrame(
	{
		"name": ["Ava", "Ben", "Cara", "Dan"],
		"age": [20, 17, 22, 19],
		"score": [88, 72, 95, 64],
		"city": ["London", "Paris", "London", "Rome"],
	}
)


# Filter rows where one condition is true.
adults = students[students["age"] >= 18]
print(adults)

# Filter rows with a text value.
london_students = students[students["city"] == "London"]
print(london_students)

# Use & for AND. Put each condition in parentheses.
high_scores = students[(students["score"] >= 80) & (students["age"] >= 18)]
print(high_scores)

# Use | for OR.
young_or_high_scoring = students[(students["age"] < 18) | (students["score"] >= 90)]
print(young_or_high_scoring)

# Use ~ to reverse a condition (NOT).
not_in_london = students[~(students["city"] == "London")]
print(not_in_london)

# Select rows whose city is in a list of cities.
selected_cities = students[students["city"].isin(["London", "Rome"])]
print(selected_cities)

# Filter values between two limits, including both limits.
middle_scores = students[students["score"].between(70, 90)]
print(middle_scores)

# Helpful reminders:
# - Use == to compare values (not =).
# - Use &, |, and ~ instead of and, or, and not.
# - Add parentheses around every condition.
