# This program shows the how to create and use variables in Python

# Variables are used to store data that can be used later in the program.

# Creating variables and assigning values to them.
name = "Vashu Tyagi"  # String variable
age = 25  # Integer variable
height = 5.9  # Float variable
boolean_value = True  # Boolean variable
a = b = c = 10  # Multiple variables assigned the same value
a, b, c = 10, "Python", True  # Multiple variables assigned different values

# Displaying the values of the variables using the print() function.
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Boolean Value:", boolean_value)
print("Multiple Variables:", a, b, c)

# Now how to use variables in expressions and calculations.
# Using variables in expressions.
sum_of_numbers = a + age  # Adding two variables
print("Sum of a and age:", sum_of_numbers)

# Using variables in string concatenation.
greeting = "Hello, " + name + "! You are " + \
    str(age) + " years old."  # Concatenating strings and variables
print(greeting)

# Now how to use variables in f-strings for better formatting.
greeting_fstring = f"Hello, {name}! You are {age} years old."
print(greeting_fstring)

# How to check variable types using the type() function.
print("Type of name variable:", type(name))
print("Type of age variable:", type(age))
print("Type of height variable:", type(height))
print("Type of boolean_value variable:", type(boolean_value))


# Local and global variables
# Local variables are defined inside a function and can only be accessed within that function.

def my_function():
    local_variable = "I am a local variable"
    print(local_variable)  # This will work


# Global variables are defined outside of any function and can be accessed from anywhere in the program.
global_variable = "I am a global variable"
print(global_variable)  # This will work
