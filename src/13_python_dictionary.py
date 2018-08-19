"""
cube finder
"""
def cuber(till):
	d = {}
	for i in range(1, till + 1):
		d[i] = i ** 3
	return d

print(cuber(10))

"""
word counter
"""

def word_counter(word):
	d = {}
	for w in word:
		d[w] = word.count(w)
	return d

print(word_counter("missiipi"))
