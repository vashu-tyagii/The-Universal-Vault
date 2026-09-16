# This Program shows the how to use operators in Python.

# There are different types of operators in Python,
# such as arithmetic, relational, logical, bitwise,assignment, ternary, and identity operators.

# Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators:")
print("Addition:", a + b)  # Addition
print("Subtraction:", a - b)  # Subtraction
print("Multiplication:", a * b)  # Multiplication
print("Division:", a / b)  # Division
print("Floor Division:", a // b)  # Floor Division Output: 2
print("Modulus:", a % b)  # Modulus Output: 0
print("Exponentiation:", a ** b)  # Exponentiation Output: 100000

# Relational Operators / Cmparison Operators
print("\nRelational Operators:")
print("Equal to:", a == b)  # Equal to
print("Not equal to:", a != b)  # Not equal to
print("Greater than:", a > b)  # Greater than
print("Less than:", a < b)  # Less than
print("Greater than or equal to:", a >= b)  # Greater than or equal to
print("Less than or equal to:", a <= b)  # Less than or equal to

# Logical Operators
print("\nLogical Operators:")
x = True
y = False
print("Logical AND:", x and y)  # Logical AND
# the output of the logical AND operator is True only if both operands are True, otherwise it returns False.
print("Logical OR:", x or y)  # Logical OR
# the output of the logical OR operator is True if at least one of the operands is True, otherwise it returns False.
print("Logical NOT:", not x)  # Logical NOT
# the output of the logical NOT operator is True if the operand is False, and it returns False if the operand is True.


# Bitwise Operators
print("\nBitwise Operators:")
x = 10  # Binary: 1010
y = 4   # Binary: 0100
print("Bitwise AND:", x & y)  # Bitwise AND Output: 0
# the output of the bitwise AND operator is 1 only if both bits are 1, otherwise it returns 0.
print("Bitwise OR:", x | y)  # Bitwise OR Output: 14
# the output of the bitwise OR operator is 1 if at least one of the bits is 1, otherwise it returns 0.
print("Bitwise XOR:", x ^ y)  # Bitwise XOR Output: 14
# the output of the bitwise XOR operator is 1 if the bits are different, otherwise it returns 0.
print("Bitwise NOT:", ~x)  # Bitwise NOT Output: -11
# the output of the bitwise NOT operator is the one's complement of the number, which means it flips all the bits of the number.

# Assignment Operators
print("\nAssignment Operators:")
x = 5
print("Initial value of x:", x)
x += 3  # Equivalent to x = x + 3
print("After x += 3:", x)
x -= 2  # Equivalent to x = x - 2
print("After x -= 2:", x)
x *= 4  # Equivalent to x = x * 4
print("After x *= 4:", x)
x /= 2  # Equivalent to x = x / 2
print("After x /= 2:", x)

# Ternary Operator
print("\nTernary Operator:")
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# Identity Operators
print("\nIdentity Operators:")
x = 10
y = 10
print("x is y:", x is y)
# Identity operator checks if both variables point to the same object in memory.
print("x is not y:", x is not y)
# Identity operator checks if both variables do not point to the same object in memory.