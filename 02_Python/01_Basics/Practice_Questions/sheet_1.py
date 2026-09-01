# # Create variables for your name (string), age (int), height in meters (float), and whether you're a student (boolean). Print all of them.
# name = input('Enter your name :')
# age = int(input('Enter your age :'))
# height = float(input('Enter your height :'))

# print(f"Hi {name} , your age is {age} and your height is {height}")
# # Check and print the type of each variable using type().
# print(
#     f"Type of each variable : \n {type(name)} \n {type(age)} \n {type(height)}")
# # Convert a string "25" into an integer and add 5 to it. Print the result.
# sting_value = input('\n\nEnter any Number :')
# num = int(sting_value)
# print(
#     f"Converting STR value {sting_value} {type(sting_value)} \ninto Int {num} {type(num)} \nand adding 5 {num + 5}")
# # Create two variables a = 10 and b = 3. Print the result of a/b, a//b, and a%b — explain in a comment what the difference is between / and //.
a = 10
b = 3

# / performs true division and returns a float result
f1 = a/b
# // performs floor division and returns an integer result (rounds down to nearest whole number)
f2 = a//b
# % returns the remainder after division
f3 = a % b

print(f"/ : {f1} \t //: {f2} \t % : {f3}")
