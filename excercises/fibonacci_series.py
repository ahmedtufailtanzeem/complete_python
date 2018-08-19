until = 20
series = []
for i in range(until):
	if i == 0 or i == 1:
		series.append(i)
	else:
		series.append(series[i - 1] + series[i - 2])
print(series)
