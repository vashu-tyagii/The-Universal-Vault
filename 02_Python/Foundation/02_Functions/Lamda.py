"""Lambda Functions in Python

A lambda function is a small anonymous function.
It is written in a single line and can take any number of arguments,
but only one expression.

Syntax:
    lambda arguments: expression

Use cases:
- short, one-time functions
- passing functions to other functions like map(), filter(), sort(), etc.
- writing compact code without a full def block

Note:
- lambda functions are not ideal for complex logic
- they are best for simple expressions
"""

# Example 1: Simple lambda with one argument
square = lambda x: x * x # type: ignore
print("Square of 5:", square(5)) # type: ignore

# Example 2: Lambda with multiple arguments
add = lambda a, b: a + b # type: ignore
print("Addition:", add(10, 20)) # type: ignore

# Example 3: Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n * n, numbers))
print("Squares:", squares)

# Example 4: Using lambda with filter()
# Keep only even numbers
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example 5: Using lambda with sorted()
students = [("Alice", 90), ("Bob", 75), ("Charlie", 95)]
# Sort by score (second element in each tuple)
sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted students by score:", sorted_students)

# Example 6: lambda inside another function

def apply_operation(x, operation): # type: ignore
    return operation(x) # type: ignore

# `lambda n: n * 3 + 2` ek chhota anonymous function hai.
# apply_operation() ise 8 ke saath call karta hai:
# 8 * 3 + 2 = 26, aur result mein 26 store hota hai.
result = apply_operation(8, lambda n: n * 3 + 2) # type: ignore
print("Custom operation result:", result) # type: ignore

# Example 7: lambda with conditional expression
# Return 'even' if number is even else 'odd'
check_even = lambda n: "even" if n % 2 == 0 else "odd" # type: ignore
print("Check 6:", check_even(6))
print("Check 7:", check_even(7))

# Important notes:
# 1. Lambda is anonymous and usually used for short tasks.
# 2. It can only contain one expression, not statements like loops/if blocks.
# 3. For complex logic, use a regular def function instead.

# Example 8: Traditional function vs lambda

def double_value(x): # type: ignore
    return x * 2 # type: ignore

print("Using def:", double_value(4))
print("Using lambda:", (lambda x: x * 2)(4))
