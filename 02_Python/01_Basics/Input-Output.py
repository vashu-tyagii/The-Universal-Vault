# This program demonstrates how to take user input and display it back to the console.

# The input() function is used to get input from the user.

user_input = input("Please enter something: ")
user_input_fixed_string = 'vashu Tyagi'
user_input_fixed_number = 42



# The print() function is used to display the input back to the console.

print("You entered:", user_input)
print("Fixed string:", user_input_fixed_string)
print("Fixed number:", user_input_fixed_number)

# Printing using f-strings for better formatting.

print(f"You entered: {user_input}")

# Printing using Variable concatenation.

print("You entered: " + user_input)

# Input can also be converted to other data types, such as integers or floats.

# Integer input
user_input_int = int(input("Please enter an integer: "))
print("You entered the integer:", user_input_int)

# Int is used to convert the input string to an integer. If the input is not a valid integer, it will raise a ValueError.

# Float input

user_input_float = float(input("Please enter a float: "))
print("You entered the float:", user_input_float)

# Float is used to convert the input string to a float. If the input is not a valid float, it will raise a ValueError.

# String input

user_input_string = input("Please enter a string: ")
print("You entered the string:", user_input_string)

