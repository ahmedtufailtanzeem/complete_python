# Use enumerate function to get position in list

def find_position(words, to_search):
	for pos, word in enumerate(words):
		if word == to_search:
			return pos
	return -1

print(find_position(["a", "b", "c", "d", "tanzeem"], "ahmed"))
print(find_position(["a", "b", "c", "d", "tanzeem"], "c"))