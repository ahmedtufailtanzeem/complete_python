# unordered collection of key-value pairs
# limitation of list in representing real world data

user_info = {'name': 'tanzeem', 'age': 31}
print(user_info)

# second method
user_info = dict(name='tanzeem ahmed', age=31)
print(user_info)

# creating using constructors
t = tuple()
l = list()
d = dict()
print(type(t))
print(type(l))
print(type(d))

t = ()
l = []
d = {}
print(type(t))
print(type(l))
print(type(d))

# since dictionaries are unordered there is no index access using name
print(user_info['age'])

# Adding data to dictionary
user_info['bike'] = None
print(user_info)

# Check if key is present
if "age" in user_info:
	print("'age' key is present")

# Check if value is present
if "tanzeem ahmed" in user_info.values():
	print(f"value is present")

# keys() --> return a list of dict_keys
# values() --> return a list of dict_values
# items() --> return a list of dict_tuple

for name, age in user_info.items():
	print(name, age)

# Merging 2 dictionaries

d1 = {'name':'Maira'}
d2 = dict(age = 3)
d1.update(d2)
print(d1)

# add and delete data
d1['married'] = True
print(d1['married'])

# Remove random element using popitem()
print(d1)
d1.pop('married')
print(d1)

d1.popitem()
print(d1)

# Below will fail if key is not present, use get method it wil return None if not present
# print(d1['married'])

print(d1.get('married','default not marries'))

# fromkeys - Assign same values to multiple keys
# Args can be anything that is iterable. EX: Tuple, List, String etc
d = dict.fromkeys(['name', 'age', 'gender'], "Unknown")
print(d)

# Create a copy
d_copy = d1.copy()
print(d_copy == d1.copy()) # True compares value
print(d_copy is d1.copy()) # Compares location

d = d1 # Will just create reference to same dictionary. Modification on one modifies the other