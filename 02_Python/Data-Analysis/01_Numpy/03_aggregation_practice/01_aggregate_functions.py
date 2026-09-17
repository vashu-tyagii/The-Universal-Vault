"""
Topic: Aggregate functions — sum(), mean(), min(), max(), std()

Aggregate functions reduce an array to one value (or to values along an
axis).  They are useful for summarizing numerical data.

Common functions:
	np.sum(array)   - total of the values
	np.mean(array)  - arithmetic average

	np.min(array)   - smallest value
	np.max(array)   - largest value
	np.std(array)   - standard deviation; spread around the mean

For a 2-D array, axis=0 works down the rows and returns one value per column;
axis=1 works across the columns and returns one value per row.  The `keepdims`
argument preserves the reduced dimension when set to True.
"""

import numpy as np


# Example data: rows represent students and columns represent subjects.
scores = np.array(
	[
		[80, 75, 90],
		[65, 88, 72],
		[92, 95, 89],
	]
)

# Aggregates for every value in the array.
total = np.sum(scores)       # 746
average = np.mean(scores)    # 82.888...
lowest = np.min(scores)      # 65
highest = np.max(scores)     # 95
spread = np.std(scores)      # standard deviation of all scores
# Aggregates by axis.
subject_averages = np.mean(scores, axis=0)  # one average per subject
student_totals = np.sum(scores, axis=1)    # one total per student

print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Lowest: {lowest}")
print(f"Highest: {highest}")
print(f"Standard deviation: {spread:.2f}")
print(f"Subject averages: {subject_averages}")
print(f"Student totals: {student_totals}")

# NumPy also provides methods with the same behavior:
# scores.sum(), scores.mean(), scores.min(), scores.max(), scores.std()
