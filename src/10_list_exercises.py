"""
# Positive numbers 1 to 10
numbers = list(range(1, 11))
print(numbers)

# Print -ve of the above number
negative_numbers = [-num for num in numbers]
print(negative_numbers)
"""

""" 
# Square of numbers

numbers = list(range(1,6))
squares = [num*num for num in numbers]
print(squares)

"""

""" Print in reverse
words = ["a", "b", "c", "d"]
rev_words = []
for word in words[::-1]:
	rev_words.append(word)
print(rev_words)


words = ["a", "b", "c", "d"]
rev_words = []
for i in range(len(words)):
	rev_words.append(words.pop())
print(rev_words)
"""

""" Word reverse in list

word_list = ["Apple", "Mango", "Banana"]
rev_word_list = []
for word in word_list:
	rev_word_list.append(word[::-1])
print(rev_word_list)

"""

""" Take list of numbers and create odd and even list as part of sub list

all_numbers = list(range(1, 11))
odd_numbers = []
even_numbers = []
for num in all_numbers:
	even_numbers.append(num) if num % 2 == 0 else odd_numbers.append(num)
print([even_numbers, odd_numbers])
"""

""" Intersection of List
list_1 = [1, 2, 5, 6]
list_2 = [3, 4, 2, 6, 1, 9, 0]
list_3 = [3, 4, 2]
intersection = []

for num in list_1:
	if num in list_2 and num in list_3:
		intersection.append(num)

print(intersection)
"""

""" Greatest difference between list elements

numbers = [10, 20, 40, 1]
print(max(numbers) - min(numbers))
"""

inner_list = [1, 2, 3, [4, 5], [6, 7], 8, 9]
count = 0
for ele in inner_list:
	if type(ele) == list:
		count += 1
print(count)
