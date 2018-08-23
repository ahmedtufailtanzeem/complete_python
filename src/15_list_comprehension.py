# List comprehension exercises - Print odd numbers
words = ['abc', 'def', 'ghi']
rev_words = [word[::-1] for word in words]
print(rev_words)

# List comprehension exercises - Print even numbers with if
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# List comprehension - print type only numbers

mixed = [1, 1.2, 3, [1, 2, 3], "a", 6, "happy", {}]
numbers = [str(i) for i in mixed if (type(i) == int or type(i) == float)]
print(numbers)

odd_even = ["odd" if i % 2 != 0 else "even" for i in range(1, 11)]
print(odd_even)
