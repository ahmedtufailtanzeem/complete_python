add = lambda a, b: a + b
mul = lambda a, b: a * b

# This is anonymous despite assigning a value so <lamda> is printed
print(add)
print(add(1, 2))
print(mul(1, 2))

# Odd or Even using lamda

is_even = lambda a: a % 2 == 0
print(is_even(8))
print(is_even(9))

last_char = lambda word : word[-1]
print(last_char("Nussi"))

# length > 5
is_long = lambda word:True if len(word) > 5 else False  # len(word) > 5
print(is_long("a"))
print(is_long("tanzeem"))