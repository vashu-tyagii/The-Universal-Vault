# Take a user's name as input and print "Hello, [name]!"
name = input('Enter Your Name :')
print(f"Hello, {name}")
# Take two numbers as input (as strings by default) and print their sum (remember to convert to int/float first).
num1, num2 = input("Enter two separated by ',' value: ").split(',') 
num1 = int(num1)
num2 = int(num2)
print(f"Sum : {num1 + num2}")
# Take a user's age as input and print whether they'll be eligible to vote this year (age >= 18).
age = int(input("Enter Your age : "))
if age >= 18 :
    print("Eligible")