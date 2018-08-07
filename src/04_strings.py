print("\nString concatination")
first_name = "tanzeem"
last_name = "ahmed"

print(first_name + " " + last_name)
# print(first_name + 3) Will result in error, we must convert it to string
print(first_name + " 3")
print(first_name + " " + str(3))

# string multiplication is Allowed
print("Couchbase " * 3)

# String indexing
print("\nString indexing")
language = "Python"
print(language[0])
print(language[2])
print(language[-1])
print(language[-6])

# String slicing[start argument: stop argument]
#-6  -5  -4  -3  -2  -1
# 0   1   2   3   4   5
# p	  y	  t	  h	  o	  n
print("\nString slicing[start argument: stop argument]")
print(language[0:2])
print(language[2:4])
print(language[:])
print(language[2:]) # Till end
print(language[:4]) # From start
print(language[-6:-1])
print(language[-6:4])

# Step/stride argument
print("\nStep argument")
print("tanzeem"[::2])
print("tanzeem"[0::2])
print("tanzeem"[:5:2])
print("tanzeem"[::-1]) # Reverse the string using -ve stride
print("tanzeem"[::-2]) # Reverse the string using -ve stride