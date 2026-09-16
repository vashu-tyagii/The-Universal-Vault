# This program demonstrates how to create loops in Python.

# types of loops in Python:
# 1. for loop
# 2. while loop
# 3. nested loop

# 1. for loop
print("=" * 50)
print("FOR LOOP IN PYTHON")
print("=" * 50)

fruits = ["apple", "banana", "cherry", "date"]
print("\nIterating through a list of fruits:")
for fruit in fruits:
    print(f"- {fruit}")

print("\nUsing range() to iterate over numbers:")
for number in range(1, 6):
    print(f"Number: {number}")

# 2. while loop
print("\n" + "=" * 50)
print("WHILE LOOP IN PYTHON")
print("=" * 50)

count = 1
while count <= 5:
    print(f"Count is {count}")
    count += 1

# 3. nested loop
print("\n" + "=" * 50)
print("NESTED LOOP IN PYTHON")
print("=" * 50)

print("\nMultiplication table from 1 to 3:")
for i in range(1, 3):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("---")

# Demonstrating break and continue in a loop
print("\n" + "=" * 50)
print("BREAK AND CONTINUE")
print("=" * 50)

for number in range(1, 11):
    if number == 8:
        print("Reached 8, breaking out of loop")
        break
    if number % 2 == 0:
        print(f"Skipping even number {number}")
        continue
    print(f"Processing odd number {number}")
