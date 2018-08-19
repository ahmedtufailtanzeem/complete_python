"""
print("Slicing, strides behave like a String")

# Can contain any type
mix = ["1", 2, "Three", "Four"]

# Print all list
print(mix[:])

# Print from 2nd item
print(mix[1:])

# Print till 2nd item
print(mix[:2])

# Print list in reverse order
print(mix[::-1])

# Replace item at position 2
mix[2] = 3
print(mix)

# Replace item from position
numbers = ["one", "two", "three", "four"]
numbers[1:] = [1, 2, 3]
print(numbers)

# Replace till end
numbers = ["one", "two", "three", "four"]
numbers[1:] = [1, 2, 3, 4, 5]
print(numbers)

# Replace with start and end depends on right side assignment
numbers = ["one", "two", "three", "four"]
numbers[1:] = [1]
print(numbers)

# The above are confusing avoid them


# Adding items to list
fruits = []
fruits.append("Mango")
fruits.append("Apple")
print(fruits)

# Insert at specific position
fruits.insert(1, "grapes")
print(fruits)

# Insert at position greater than size of list
fruits.insert(20, "Kiwi")
print(fruits)

# Concatinate using + or extends
vegetables = ["cucumber", "carrot"]
fruits = fruits + vegetables
print(fruits)

# Using extends
fruits.extend(vegetables)
print(fruits)

# Don't use appends, else will add as inner list
fruits.append(vegetables)
print(fruits)

# Pop/remove elements
fruits.pop()
print(fruits)

# Pop at specific element.. Result of pop is element removed
fruits.pop(1)
print(fruits)

# delete at specific position
del fruits[2]
print(fruits)

# What if I don't know if element is present, will fail if element to remove is not in list
fruits.remove("Mango")
print(fruits)

# ValueError if element to remove is not present
# fruits.remove("Banana")
# print(fruits)

# If more than one occurence then it will remove first occurence
# fruits.remove('a')
# print(fruits)


# Check if element is present in the list
print("carrot" in fruits)
print("plums" in fruits)

# More String functions
characters = ["f", "d", "a", "c", "b"]

# sort with actual String updated
characters.sort()
print(characters)

# reverse
characters.reverse()
print(characters)

# sort with out changing the actual list
print(sorted(characters))

# copy
chars = characters.copy()
print(chars)

# count
characters.append("b")
print(characters.count("b"))

# Clear the list
characters.clear()
print(characters)

# Comparing list in Python
list_1 = ["a", "b", "c"]
list_1_copy = ["a", "b", "c"]
list_2 = ["a", "b", "d"]
list_3 = list_1

print(list_1 == list_1_copy) # Checks for value
print(list_1 is list_1_copy)
print(list_1 is list_3)  # is check memory location

# split vs join
user_info = "tanzeem ahmed 31"
user_info = user_info.split(" ")
print(user_info)

user_info = ",".join(user_info)
print(user_info)

# Strings are immutable, List are mutable

# Looping in list

for fruit in fruits:
	print(fruit)

i = 0
while i < len(fruits):
	print(fruits[i])
	i+= 1

"""

# Generate list with Range function
numbers_1_10 = list(range(1,11))
print(numbers_1_10)

numbers_1_10.append(1)
print(numbers_1_10)

# Index in List
print(numbers_1_10.index(1))
print(numbers_1_10.index(1, 5, 9))  # Value error if not found in the start & stop range