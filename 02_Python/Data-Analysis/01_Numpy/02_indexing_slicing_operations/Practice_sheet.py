"""
Topic: Indexing, Slicing, Operations — 10 Practice Questions
"""
import numpy as np  # type: ignore
# 1. Create a 1D array [5, 10, 15, 20, 25, 30]. Print the first element,
#    the last element (using negative indexing), and the third element.
arr = np.arange(5, 31, 5)
print(f"First Element : {arr[0]}")
print(f"Last Element : {arr[-1]}")
print(f"Third Element : {arr[2]}")
# 2. From the same array, slice out the middle 3 elements ([15, 20, 25]).
print(f"Three Element : {arr[2:5]}")

# 3. Create a 2D array (3x3, any numbers). Print the element at row 1,
#    column 2 using [row, col] indexing.
matrix = np.arange(1, 10)
matrix = matrix.reshape(3, 3)
print("2 Elements :", matrix[1, 2])
# 4. From the same 2D array, print the entire second row, and separately
#    the entire first column.
print("2nd Row :", matrix[1])
print("1st Column :", matrix[:, 0])
# 5. Create two 1D arrays of 5 numbers each. Add them together, then
#    subtract the second from the first, and print both results.
arr_1d = np.arange(1, 6)
arr_1d_2 = np.arange(1, 6)
print("Adding By Two :", arr_1d + arr_1d_2)
print("Subtracting Arrays :", arr_1d - arr_1d_2)
# 6. Create a 1D array of 6 numbers. Multiply every element by 3, then
#    divide every element by 2. Print both results.
arr_1d_3 = np.arange(1, 7)
print(f"Multiply By Three  : {arr_1d_3 * 3}")
print(f"Divide By Two : {arr_1d_3 / 2}")
# 7. Create a 1D array of 10 numbers (any values). Use a comparison
#    operation to print which elements are greater than 15.
arr_1d_4 = np.arange(10, 20)
greater_than_15_mask = arr_1d_4 > 15
print(f"Greater Than 15 Mask : {greater_than_15_mask}")
# 8. Using boolean indexing, filter the same array from Q7 to show only
#    the actual values greater than 15 (not True/False, the real numbers).
greater_than_15 = arr_1d_4[arr_1d_4 > 15]
print(f"Values Greater Than 15 : {greater_than_15}")

# 9. Create a 1D array of 12 numbers, then reshape it into a (3, 4) 2D array.
#    Print the reshaped array and confirm its shape.
arr_12 = np.arange(1, 13)
reshaped_arr = arr_12.reshape(3, 4)
print("Reshaped Array :")
print(reshaped_arr)
print(f"Shape : {reshaped_arr.shape}")

# 10. Create a 2D array of shape (2, 3). Try to reshape it into shape (2, 4)
#     and observe what happens (it should raise an error) — wrap it in a
#     try/except and print a message explaining why it failed.
array_2x3 = np.arange(1, 7).reshape(2, 3)
try:
    array_2x4 = array_2x3.reshape(2, 4)
except ValueError as error:
    print(
        f"Reshape failed: a (2, 3) array has 6 elements, but (2, 4) requires 8. {error}")
