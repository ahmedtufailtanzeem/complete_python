"""
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Hello {} {}".format(first_name, last_name))

# The value type from Input is always a String

operand_1 = int(input("Enter 1st operand: "))
operand_2 = int(input("Enter 2nd operand: "))
print("sum is " + str(operand_1 + operand_2))

# Conversions

int = int("1001")
print(int)
floating = float("3.17")
print(floating)
strings = str("1")
print(strings)

# Multiple inputs in one go
name, age = input("Enter name and then age separated by ,").split(",")
print("Hello {}, You are {} years old!!!".format(name, age))
print(f"Hello {name}, You are just {age}!!!")

"""
# Exercise
x,y,z = input("Enter 3 space separated values: ").split(" ")
print(f"Average of {x}, {y} and {z} is {(int(x)+int(y)+int(z))/3}")