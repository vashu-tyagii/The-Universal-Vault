from typing import Any

# Functions
# A function is a reusable block of code that performs a specific task.
# It is defined with `def` and called by writing its name followed by `()`.


def fun() -> None:
    """Print a welcome message."""
    print("Welcome to GFG")


fun()

# Function arguments
# Arguments are values passed to a function when it is called.


def even_odd(x: int) -> str:
    """Return whether an integer is even or odd."""
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_odd(16))
print(even_odd(7))

# Types of function arguments

# 1. Default arguments
# A default argument has a predefined value that is used when no value is passed.


def my_fun(x: int, y: int = 50) -> None:
    """Display a required argument and an argument with a default value."""
    print("x: ", x)
    print("y: ", y)


my_fun(10)

# 2. Keyword arguments
# Keyword arguments are passed using parameter names, so their order does not matter.


def student(fname: str, lname: str) -> None:
    """Display a student's first and last name."""
    print(fname, lname)


student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# 3. Positional arguments
# Positional arguments are assigned to parameters according to their order.

def name_age(name: str | int, age: int | str) -> None:
    """Display a name and age using positional arguments."""
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
name_age("Olivia", 27)

print("Case-2:")
name_age(27, "Olivia")

# 4. Arbitrary arguments
# Arbitrary arguments allow a function to accept any number of values:
# *args stores extra positional arguments in a tuple.
# **kwargs stores extra keyword arguments in a dictionary.


def my_fun_args(*args: Any, **kwargs: Any) -> None:
    """Display arbitrary positional and keyword arguments."""
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")


my_fun_args("Hey", "Welcome", first="Geeks", mid="for", last="Geeks")

# Nested functions
# A function defined inside another function is called an inner or nested function.
# It can access variables defined in the enclosing function.


def f1() -> None:
    """Demonstrate a nested function and an enclosing variable."""
    s = 'I love GeeksForGeeks'

    def f2() -> None:
        print(s)

    f2()


f1()

# Return statement
# `return` ends a function and sends a value back to the caller.
# A function can return any data type, multiple values as a tuple, or None.


def sq_value(num: int) -> int:
    """Return the square of a number."""
    return num**2


print(sq_value(2))
print(sq_value(-4))
