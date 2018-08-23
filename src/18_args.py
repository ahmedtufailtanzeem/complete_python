# *args and **args in python will help make flexible functions
# Make sure *args always follows positional else it's an error
def calc(operation, *args):
	# print(args)
	if operation == "add":
		sum = 0
		for i in args:
			sum += i
		return sum
	else:
		mul = 1
		for i in args:
			mul *= i
		return mul


print(calc("add", 2, 3, 4))
print(calc("mul", 2, 3, 4))

# *args as argument
# This will be changes to tuple inside tuple ((1, 2, 3, 4, 5),)
# print(calc("add", (1, 2, 3, 4, 5)))
# unpack list/tuple using *
print(calc("mul", *[1, 2, 3, 4, 5]))
print(calc("add", *(1, 2, 3, 4, 5)))


def cube_calc(*args):
	if not len(args):
		print("Enter some arguments")
	else:
		return [i ** 3 for i in args]


print(cube_calc())
print(cube_calc(*[1, 2, 3, 4, 5]))


# **kwargs - keyword arguments, don't confuse with positional and named parameters
# converts to dict unlike *args will convert as tuple

def person_info(**kwargs):
	for k, v in kwargs.items():
		print(k, v)


person_info(name="tanzeem", age=31)

# dictionary unpacking using **
person_info(**{'name': "tanzeem", 'age': 31})

# Follow PADK rule to remember correct order
def func(positional, *args, named='default', **kwargs):
	pass
