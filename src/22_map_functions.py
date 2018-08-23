# Using map functions with lambda
# We can achieve the same using list comprehension
# Makes code much readable using lambdas
squares = map(lambda number: number ** 2, list(range(1, 11)))
print(list(squares))

# Use map when you have to perform something using function

words = ["a", "very", "sad", "ending"]
length = list(map(len, words))
print(length)