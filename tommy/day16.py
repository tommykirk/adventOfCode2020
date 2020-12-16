

with open('day16.txt', 'r') as file:
	text = file.read().split('\n\n')


	validNumSet = set()
	for rule in text[0].split('\n'):
		firstRange = rule.split(' or ')[0].split()[-1]
		secondRange = rule.split(' or ')[1].strip()
		min1, max1 = [int(x) for x in firstRange.split('-')]
		min2, max2 = [int(x) for x in secondRange.split('-')]
		for i in range(min1, max1 + 1):
			validNumSet.add(i)
		for i in range(min2, max2 + 1):
			validNumSet.add(i)

	print(validNumSet)

	sumOfInvailds = 0

	otherTickets = text[2].split('\n')[1:-1]
	print(otherTickets)
	for ticket in otherTickets:
		fieldVals = [int(x) for x in ticket.strip().split(',')]
		for val in fieldVals:
			if val in validNumSet:
				continue
			else:
				sumOfInvailds += val

	print(sumOfInvailds)


