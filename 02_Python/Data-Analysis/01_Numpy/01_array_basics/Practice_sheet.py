"""
Topic: Array Basics — 10 Easy Level Practice Questions
(Covers: array vs list, creating 1D/2D arrays, shape/size/ndim, zeros/ones/arrange)

Solve without looking at notes. Run each one and check the output.
"""
import numpy as np  # type: ignore
# 1. Create a 1D NumPy array with values [10, 20, 30, 40, 50] and print it.
arr = np.array([10, 20, 30, 40, 50])
print(f"\nArray :{arr}")

# 2. Create a Python list with the same values, convert it to a NumPy array
#    using np.array(), and print its type using type().
lst = [10, 20, 30, 40, 50]
arr2 = np.array(lst)
print(f"\nArray :{arr2}")

# 3. Create a 2D array representing a 3x3 grid of your choice (any 9 numbers),
#    and print it.
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array : {arr_2d}")
# 4. For the 2D array from Q3, print its shape, size, and ndim.
print(
    f"\nArray Shape :{arr_2d.shape} \nArray Size :{arr_2d.size} \nArray Type :{arr_2d.ndim}")
# 5. Create a 1D array of 10 zeros using np.zeros().
arr_1d_zeros = np.zeros(4, dtype=int)
print(arr_1d_zeros)
# 6. Create a 2D array of shape (3, 4) filled with ones using np.ones().
arr_2d_one = np.ones((2, 3), dtype=int)
print(arr_2d_one)
# 7. Create an array of numbers from 0 to 20 (exclusive) using np.arange().
arr_arrange = np.arange(0, 21)
print(arr_arrange)
# 8. Create an array of numbers from 10 to 50, stepping by 5, using np.arange()
#    with a step value.
arr_arrange_step = np.arange(10, 51, 5)
print(arr_arrange_step)
# 9. Create a 1D array of any 6 numbers, then reshape it into a 2D array of
#    shape (2, 3) using .reshape().
arr1d = np.arange(1, 7)
reshape_arr = arr1d.reshape((2, 3))
print(reshape_arr)
# 10. Create two separate arrays: one using a Python list and math (e.g.,
#     [i for i in range(5)]), and one directly using np.arange(5). Compare
#     them using == and print whether all elements match.
array_from_list = np.array([i for i in range(5)])
array_from_arrange = np.arange(5)
print("All elements match:",np.all(array_from_list == array_from_arrange))
