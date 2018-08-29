# Using list comprehension
even_number_less_than_10 = [i for i in range(1, 11) if i % 2 == 0]
print(even_number_less_than_10)

# Using Filter function

even_number_less_than_10 = list(filter(lambda a: a % 2 == 0, list(range(1, 11))))
print(even_number_less_than_10)


def func(number):
	return str(number)


result = filter(func, [1, 22, 333, ""])
print(list(result))  # [1, 22, 333] Empty is evaluated to False and filtered

# map/filter return Iterator. So can be looped only once. So, convert them into Iterable types Tuple/List ect

lengths = map(len, ["a", "ab", "abc", "abcd", "abcde"])
for i in lengths:
	print(i, end=" ")

# Below won't print since it is Iterator and already reached the end using next-->next
for i in lengths:
	print(i, end=" ")

# cast iterator intoIterable using list, tuple
