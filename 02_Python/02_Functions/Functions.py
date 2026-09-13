from typing import Any


def fun() -> None:
    print("Welcome to GFG")


fun()

# Function Arguments


def even_odd(x: int) -> str:
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_odd(16))
print(even_odd(7))

# Types of Function Arguments

#  Default argument: Default argument use a predefined value when no value is passed during the function call.


def my_fun(x: int, y: int = 50) -> None:
    print("x: ", x)
    print("y: ", y)


my_fun(10)

# 2. Keyword Arguments: pass values using parameter names, so argument order does not matter.


def student(fname: str, lname: str) -> None:
    print(fname, lname)


student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# 3. Positional Arguments: values are assigned to parameters based on their order in the function call.

def name_age(name: str | int, age: int | str) -> None:
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
name_age("Olivia", 27)

print("Case-2:")
name_age(27, "Olivia")

# 4. Arbitrary Arguments: allow functions to accept multiple values. This is done using two special symbols:


def my_fun_args(*args: Any, **kwargs: Any) -> None:
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")


my_fun_args("Hey", "Welcome", first="Geeks", mid="for", last="Geeks")

# Function within Functions
# A function defined inside another function is called an inner function (or nested function). It is used to organize related logic and access variables from the outer function.


def f1() -> None:
    s = 'I love GeeksForGeeks'

    def f2() -> None:
        print(s)

    f2()


f1()

# Return Statement
# Return is used to end a function and send a value back to the caller. It can return any data type, multiple values (packed into a tuple), or None if no value is given.


def sq_value(num: int) -> int:
    return num**2


print(sq_value(2))
print(sq_value(-4))
