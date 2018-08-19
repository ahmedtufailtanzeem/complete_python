# immutable data structure. No further modifications allowed.
# Can store mixed type like list
# They are faster than list
days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
print(days)
# days['7'] = 'noday'

# Below is regular assignment and type will be String
assign1, assign2 = "hello", "world"

# Tuple assignment since value on rt hand side is more
assign = "hello", "world"
print(type(assign))

# 3 count
print(assign.count("world"))

# Declaring 1 element tuple always use comma
single = (1,)
print(type(single))

# tuple un packing
mon, tue, wed, thus, fri, sat, sun = days
print(tue)
print(sat)

# looping in tuples
for day in days:
	print(day)

# We can use min/max len on tuple like in list
print(max(days))
print(min(days))
print(len(days))

# We can have mixed types inside tuple, and based on type sub types can be mutable
mixed = ('apple', 'banana', ['raddish', 'carrot'])
print(mixed)
mixed[2].pop()
print(mixed)


# function returning more than 1 value

def func(num1, num2):
	return num1 + num2, num1 * num2


result = func(10, 20)
print(type(result))
print(result)

sum, mul = func(10, 20)
print(sum, mul, type(sum))

# Generating tuples using range
# nums = list(range(1, 11))
nums = tuple(range(1, 11))
print(type(nums))

# using str function gives you str in a tuple format
print(type(str(nums)))
print(str(nums))

list = ['a', 'b', 'c']
print(tuple(list))


# index
print(days.index("tuesday"))
print(days.index("wednesday", 0))
