# This program demonstrates the use of different data types in Python.

# Define a string variable
name = "Alice"
# Define an integer variable
age = 30
# Define a float variable
height = 5.7
# Define a boolean variable
is_student = True

# Print the values and their types
print("Name:", name, "Type:", type(name))
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Is Student:", is_student, "Type:", type(is_student))

# list variable
# list are used to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values.
# list are mutable, meaning you can change their content without changing their identity. Lists are defined by having values between square brackets [ ].
fruits = ["apple", "banana", "cherry"]

# All type of task we do with list

# Accessing elements
print("First fruit:", fruits[0])  # Accessing the first element
print("Second fruit:", fruits[1])  # Accessing the second element
print("Third fruit:", fruits[2])  # Accessing the third element

# appending elements , removing elements, and modifying elements
fruits.append("orange")  # Adding an element to the end of the list
print("Fruits after appending:", fruits)
fruits.remove("banana")  # Removing an element from the list
print("Fruits after removing banana:", fruits)
fruits[1] = "kiwi"  # Modifying the second element
print("Fruits after modifying second element:", fruits)

# tuple variable
# Tuples are used to store multiple items in a single variable. Tuples are ordered, unchangeable, and allow duplicate values. Tuples are defined by having values between parentheses ( ).
# Tuples are immutable, meaning you cannot change their content once they are created. However, you can create a new tuple that contains the desired changes.
colors = ("red", "green", "blue")
print("Colors:", colors, "Type:", type(colors))

# dictionary variable
person: dict[str, object] = {"name": "Bob", "age": 25, "city": "NewYork"}

# Accessing dictionary values
# Accessing the value associated with the key "name"
print("Person's name:", person["name"])
# Accessing the value associated with the key "age"
print("Person's age:", person["age"])
# Accessing the value associated with the key "city"
print("Person's city:", person["city"])

# we can also add new key-value pairs to the dictionary
person["country"] = "USA"  # Adding a new key-value pair
print("Person after adding country:", person)

# removing a key-value pair from the dictionary
del person["age"]  # Removing the key-value pair with the key "age"
print("Person after removing age:", person)

# type casting
# Converting integer to float
age_float = float(age)
print("Age as float:", age_float, "Type:", type(age_float))

