# This file contains various string formatting methods in Python, including lower, upper, strip, replace, split, join, format, and f-string.

# The file also includes examples of how to use these methods with different data types, such as strings, integers, and floats.

print("=" * 50)
print("STRING FORMATTING METHODS IN PYTHON")
print("=" * 50)

# 1. lower() - Convert string to lowercase
print("\n1. LOWER METHOD:")
text = "Hello World"
print(f"Original: {text}")
print(f"Lowercase: {text.lower()}")

# 2. upper() - Convert string to uppercase
print("\n2. UPPER METHOD:")
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")

# 3. strip() - Remove leading and trailing whitespace
print("\n3. STRIP METHOD:")
text_with_spaces = "  Python Programming  "
print(f"Original: '{text_with_spaces}'")
print(f"Stripped: '{text_with_spaces.strip()}'")

# 4. replace() - Replace substring with another substring
print("\n4. REPLACE METHOD:")
text = "Python is great. Python is powerful."
print(f"Original: {text}")
print(f"Replaced: {text.replace('Python', 'Java')}")

# 5. split() - Split string into a list
print("\n5. SPLIT METHOD:")
text = "apple, banana, orange, grape"
print(f"Original: {text}")
print(f"Split: {text.split(', ')}")

# 6. join() - Join list elements into a string
print("\n6. JOIN METHOD:")
fruits = ["apple", "banana", "orange", "grape"]
print(f"List: {fruits}")
print(f"Joined: {', '.join(fruits)}")

# 7. format() - String formatting with placeholders
print("\n7. FORMAT METHOD:")
name = "Alice"
age = 25
salary = 50000.50
print("Using format(): {} is {} years old and earns ${:.2f}".format(name, age, salary))

# 8. f-string - Modern string formatting
print("\n8. F-STRING METHOD:")
print(f"Using f-string: {name} is {age} years old and earns ${salary:.2f}")

# Additional formatting examples
print("\n" + "=" * 50)
print("ADDITIONAL FORMATTING EXAMPLES")
print("=" * 50)

# Capitalization methods
print("\n9. CAPITALIZATION METHODS:")
text = "python programming"
print(f"Original: {text}")
print(f"capitalize(): {text.capitalize()}")
print(f"title(): {text.title()}")

# String alignment
print("\n10. STRING ALIGNMENT:")
text = "Python"
print(f"Left align (20 chars): '{text.ljust(20)}'")
print(f"Right align (20 chars): '{text.rjust(20)}'")
print(f"Center align (20 chars): '{text.center(20)}'")

# Finding substrings
print("\n11. FINDING SUBSTRINGS:")
text = "Hello World"
print(f"Text: {text}")
print(f"find('World'): {text.find('World')}")
print(f"find('xyz'): {text.find('xyz')}")

# Check string properties
print("\n12. CHECK STRING PROPERTIES:")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'ABC'.isupper(): {'ABC'.isupper()}")
print(f"'abc'.islower(): {'abc'.islower()}")
