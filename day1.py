
m = set()
with open('day1.txt', 'r') as file:
	for line in file:
		nextNum = int(line)
		if 2020 - nextNum in m:
			print((2020 - nextNum) * nextNum)
		else:
			m.add(nextNum)



