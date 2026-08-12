# This program demonstrates how to create and use conditional statements in Python.

# type of conditional statements
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. short hand if statement
# 5. short hand if-else statement
# 6. match case statement (Python 3.10 and above)

# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
y = 3
if y % 2 == 0:  # type: ignore
    print("y is even")
else:
    print("y is odd")

# if-elif-else statement
z = 15
if z < 10:
    print("z is less than 10")
elif z < 20:
    print("z is between 10 and 20")
else:
    print("z is greater than or equal to 20")

# short hand if statement
a = 7
if a > 5:
    print("a is greater than 5")

# short hand if-else statement
b = 12
print("b is greater than 10") if b > 10 else print("b is not greater than 10")

# nested if statements
if x > 0:
    if x < 10:
        print("x is a positive single-digit number")
    else:
        print("x is a positive number with multiple digits")
elif x == 0: #type: ignore
    print("x is zero")
# we can also use logical operators (and, or, not) to combine multiple conditions in a single if statement.

# we can also use nested if statements, where an if statement is placed inside another if statement.
# This allows us to check for multiple conditions in a hierarchical manner.

if x > 0:
    if x < 10:
        print("x is a positive single-digit number")
    else:
        print("x is a positive number with multiple digits")

# we can use list and dictionary in conditional statements as well. For example, we can check if an item is present in a list or if a key exists in a dictionary.
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is present in the list")

my_dict: dict[str, object] = {"name": "Alice", "age": 30}
if "name" in my_dict:
    print("The key 'name' exists in the dictionary")


# match case statement (Python 3.10 and above)
# The match case statement is a new feature introduced in Python 3.10 that allows for pattern matching. It is similar to switch-case statements in other programming languages.
# Here is an example of how to use the match case statement in Python:
value = 2
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case 3:
        print("Value is 3")
    case _:
        print("Value is something else")