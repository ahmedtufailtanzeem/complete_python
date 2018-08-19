# unordered collection of unique elements
s = {1, 2, 3, 1.2, 'a', 'b'}
print(s)

# can not store list or dictionary in set. since they are not un-hashable(so it can not remove duplicates)
# s = {[], {}}

# Adding items to set
s.add(11)

# Will throw exception if 11 is not found, use discard instead
s.remove(11)

# No error
s.discard(111)

#  copy
s1 = s.copy()
print(s1)

# clear - result will show set()
s1.clear()
print(s1)

# looping

for i in s:
	print(i)

# check if present using 'in'

# | union & intersection



