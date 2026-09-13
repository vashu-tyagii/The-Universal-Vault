"""Notes and examples for map(), filter(), and reduce().

map() and filter() return lazy iterators in Python 3, so list() is used when
we want to display their results. reduce() returns one final value.
"""

from functools import reduce


numbers = [1, 2, 3, 4, 5]

# map(function, iterable): transform every item.
squares = map(lambda number: number**2, numbers)
print("Squares:", list(squares))

# map() can use multiple iterables; it stops at the shortest one.
first = [1, 2, 3]
second = [10, 20, 30]
print("Sums:", list(map(lambda a, b: a + b, first, second)))


# filter(function, iterable): keep items for which function returns True.
even_numbers = filter(lambda number: number % 2 == 0, numbers)
print("Even numbers:", list(even_numbers))

# Passing None removes false-y values such as 0, "", and None.
values = [0, "", "Python", None, 42]  # type: ignore
print("Truthy values:", list(filter(None, values)))  # type: ignore


# reduce(function, iterable, initializer): combine items into one value.
total = reduce(lambda accumulated, number: accumulated + number, numbers, 0)
product = reduce(lambda accumulated, number: accumulated * number, numbers, 1)
print("Total:", total)
print("Product:", product)


# Example pipeline: pehle filter, phir square, aur aakhir mein total.
# 1. Sirf 2 se bade numbers rakho: [3, 4, 5]
greater_than_two = filter(lambda number: number > 2, numbers)
# 2. Har number ka square nikalo: [9, 16, 25]
squared_numbers = map(lambda number: number**2, greater_than_two)
# 3. Sab squares ko jod do: 9 + 16 + 25 = 50
result = reduce(lambda accumulated, number: accumulated +
                number, squared_numbers, 0)
print("Sum of squares greater than 2:", result)
# Output:
# Sum of squares greater than 2: 50


# List comprehensions are often clearer alternatives:
# squares = [number**2 for number in numbers]
# even_numbers = [number for number in numbers if number % 2 == 0]
