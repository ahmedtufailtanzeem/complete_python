# strings, list, tuple are Iterables
# map, filter are Iterator

result = map(lambda a: a ** 2, list(range(1, 10)))
print(result)  # map object and it is Iterator so we can directly call next
print(next(result))
print(next(result))

# whereas list are Iterable
l = list(range(1, 11))
list_iterator = iter(l)
print(next(list_iterator))
