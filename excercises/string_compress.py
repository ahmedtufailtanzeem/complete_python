input = "mississippi"
count = 1
for i in range(1, len(input) + 1):
	if i == len(input):
		print(input[i - 1] + str(count), end="")
		break
	else:
		if input[i - 1] == input[i]:
			count += 1
		else:
			print(input[i - 1] + str(count), end="")
			count = 1
