# Define a function that takes in any number of lists containing function

# def func(*args):
# 	for pair in zip(*args):
# 		print(sum(pair) / len(pair))

average = lambda *args: [sum(pair) / len(pair) for pair in zip(*args)]
print(average([1, 2, 3], [4, 5, 6], [7, 8, 9]))
