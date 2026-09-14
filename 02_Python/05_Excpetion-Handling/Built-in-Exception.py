"""Built-in Exceptions in Python

Notes:
- Python has many built-in exceptions that are raised automatically when errors occur.
- They help us catch predictable errors and respond to them gracefully.
- Use try/except blocks to handle exceptions without stopping program execution.
- A broad except Exception can catch many errors, but more specific exceptions are better.
- Always keep the code in try block minimal and focused.

Common built-in exceptions:
- SyntaxError: invalid Python syntax
- IndentationError: wrong indentation
- NameError: variable/function not defined
- TypeError: operation used on wrong data type
- ValueError: correct type but invalid value
- ZeroDivisionError: division by zero
- IndexError: list index out of range
- KeyError: dictionary key not found
- FileNotFoundError: file does not exist
- AttributeError: object has no attribute
- ImportError: module import failed
- RuntimeError: generic runtime error

Best practice:
- Catch specific exceptions first.
- Use else for code that runs only when no exception occurs.
- Use finally for cleanup tasks (closing files, releasing locks).
"""

# Example 1: Handling common exceptions
print("Example 1: Handling common exceptions")

try:
    value = int("abc")
except ValueError:
    print("ValueError: Could not convert string to integer.")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero is not allowed.")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("IndexError: Index is out of range.")

print()

# Example 2: Multiple exceptions in one block
print("Example 2: Multiple exception handling")

try:
    data = {"name": "Alice"}
    print(data["age"])  # KeyError if key not found
except KeyError:
    print("KeyError: The required key does not exist.")

# Example 3: Using else and finally
print("\nExample 3: else and finally")

try:
    num = int("25")
except ValueError:
    print("Invalid input")
else:
    print("No exception occurred. Number is:", num)
finally:
    print("This always runs, whether an error happened or not.")

# Example 4: File handling with built-in exception
print("\nExample 4: FileNotFoundError")

try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("FileNotFoundError: The file was not found.")

# Example 5: Raising built-in exceptions manually
print("\nExample 5: Raising exceptions manually")

age = -2
if age < 0:
    raise ValueError("Age cannot be negative.")

# Example 6: Catching multiple exception types
print("\nExample 6: Catching multiple exceptions")

try:
    x = 10
    y = "5"
    result = x + y
except TypeError:
    print("TypeError: You cannot add an integer and a string directly.")
except ValueError:
    print("ValueError: Invalid value encountered.")

print("\nProgram finished successfully.")
