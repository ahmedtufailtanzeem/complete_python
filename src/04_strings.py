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
# -6  -5  -4  -3  -2  -1
# 0   1   2   3   4   5
# p	  y	  t	  h	  o	  n
print("\nString slicing[start argument: stop argument]")
print(language[0:2])
print(language[2:4])
print(language[:])
print(language[2:])  # Till end
print(language[:4])  # From start
print(language[-6:-1])
print(language[-6:4])

# Step/stride argument
print("\nStep argument")
print("tanzeem"[::2])
print("tanzeem"[0::2])
print("tanzeem"[:5:2])
print("tanzeem"[::-1])  # Reverse the string using -ve stride
print("tanzeem"[::-2])  # Reverse the string using -ve stride

# Print name backward
# print(input("Enter you name and see it reversed: ")[::-1])

# String functions
dots = "...."
print(dots + "    tanzeem   ".lstrip() + dots)
print(dots + "    tanzeem   ".rstrip() + dots)
print(dots + "    tanzeem   ".strip() + dots)

name = "couchbAse india"
print(len(name))
print(name.lower())
print(name.upper())
print(name.count("a"))
print(name.title()) # Caps the letter after spaces

# Exercise count
#name, word = input("Enter name and word separated by space: ").split()
#print(f"{name} has length {len(name)}")
#print(f"{word} is repeated {name.lower().count('a')} times")

# replace function
sentence_1 = "he is a amazing artist"
sentence_2 = "a apple a day keeps doctor away"
print(sentence_1.replace(" a ", " an "))
print(sentence_2.replace("a ", " an "))
print(sentence_2.replace("a", "an", 2))

# Find function
sample = "Here is the sample she is looking for"
print(sample.find("is"))
print(sample.find("is", sample.find("is")+1))

# Centre method
name = "Nusayba"
print(name.center(len(name)+1, "*"))
print(name.center(len(name)+2, "*"))
print(name.center(len(name)+3, "*"))
print(name.center(len(name)+4, "*"))

# Strings are immutable
name = "tanzeem"
print(name[0])
# name[0] = "T" Will result in error coz Strings are immutable
name = name.title()
print(name)

# Concatenation using short hand assignment
name += " Ahmed"
print(name)


# IN with Strings
name = "tanzeem"
name = ""
if name and "tan" in name: # Check in only if name is non empty
	print("You have sin/cos in your name")
else:
	print("You have nothing...")