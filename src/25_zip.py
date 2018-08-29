# convert tuple into dictionary
t = [('India', 'Delhi'), ('Australia', 'Sweden')]
print(dict(t))

# If we have more than 2 values then this will fail. dictionary only needs 2 values

# Zip function merges list into tuples

first_name = ['Tanzeem', 'Lubna', 'Nusayba', 'Ammaara']
age = [31, 24, 2, 1, 0]
last_name = ['Ahmed', 'Farheen', 'Tanzeem', 'Tanzeem']
user_info = dict(zip(first_name, last_name))
print(user_info)

user_info_tuple = list(zip(first_name, last_name, age))
print(user_info_tuple)

# Zip stops to min length of available list
# Also, remember list always maintains insertion order

# unpacking

input = [(1, 2), (3, 4), (5, 6), (7, 8)]
l1, l2 = list(zip(*input))  # reverse of zip which converts to 1
print(l1, l2)

l1 = [1, 2, 6, 8]
l2 = [2, 3, 4, 5]
l3 = []
for t in list(zip(l1, l2)):
	l3.append(max(t))
print(l1)
print(l2)
print(l3)
