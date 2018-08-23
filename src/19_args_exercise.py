def func(*args, **kwargs):
	if "reverse" in kwargs:
		return [word[::-1].title() for word in args]
	return [word.title() for word in args]


print(func(*["hello", "world"]))
print(func(*["hello", "world"], reverse=True))
