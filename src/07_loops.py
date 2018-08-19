import random

n = 10
n, sum = 10, 0
while n > 0:
	sum += n
	n -= 1

print(f"sum is {sum}")

n = "1234"
length = len(n)
i = sum = 0
while i < length:
	sum += int(n[i])
	i += 1
print(f"sum of {n} is {sum}")

name = "tanzeem ahmed t"
length = len(name)
i = 0
while i < length:
	if name[i] not in name[:i]:
		print(f"{name[i]} : {name.count(name[i])}")
	i += 1

my_name = "tanzeem"
your_name, my_length = "lubna", len(my_name)
print(my_name, my_length)

# For loop
print("Print loop forward")
for i in range(0, 10, 2):
	print(i)

print("Print loop backwards")
for i in range(10, 0, -1):
	print(i)

print("Print loop -ve backwards")
for i in range(-10, 0, 1):
	print(i)
