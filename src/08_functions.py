def add(operand_1, operand_2):
	return operand_1 + operand_2


result = add(10, 20)
print(result)

result = add("a", "bc")
print(result)


def odd_or_even(number):
	return "even" if number % 2 == 0 else "odd"


def odd_or_even_small(number):
	return number % 2 == 0


print(odd_or_even(9))
print(odd_or_even_small(101))


def return_greatest(number_1, number_2, number_3):
	# Don't do this is confusing....
	return number_1 if (number_1 > number_2 and number_1 > number_3) else (
		number_2 if number_2 > number_3 else number_3)


print(return_greatest(120, 100, 130))

# Check if Palindrome
print("Check if Palindrome")


def is_palindrome(word):
	return word == word[::-1]


print(is_palindrome("madam"))
print(is_palindrome("dad"))
print(is_palindrome("dab"))

# Fibonacci series
print("Fibonacci series")


def fibonacci(n):
	series = []
	for i in range(n):
		if i == 0 or i == 1:
			series.append(i)
		else:
			series.append(series[i - 1] + series[i - 2])
	return series


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(20))


# Default arguments - Must follow positional arguments

def full_name(first_name, last_name="unknown"):
	return first_name + " " + last_name


print(full_name("Nusayba", "Tanzeem"))
print(full_name("Nusayba"))

# scopes
x = 10


def print_x():
	global x
	x = 6
	print(f"Value of x is {x}")

print(x)
print_x()
print(x)
