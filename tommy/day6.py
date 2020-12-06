




with open('day6.txt', 'r') as file:
	totalCount = 0
	groupSet = set()
	for line in file:
		if len(line) == 1:
			totalCount += len(groupSet)
			# print(len(groupSet))
			# print(totalCount)
			groupSet = set()
		else:
			groupSet.update(c for c in line[:-1])
		# print([c for c in line])
	print(totalCount + len(groupSet))