
def remove(fieldName, fieldPos, positionToPossibleFieldNames, positionToImpossibleFieldNames, fieldNameSet, removedSet):
	if fieldName in removedSet:
		return
	removedSet.add(fieldName)
	for i in range(1, 21):
		if i == fieldPos:
			continue
		if fieldName in positionToPossibleFieldNames[i]:
			positionToPossibleFieldNames[i].remove(fieldName)
		positionToImpossibleFieldNames[i].add(fieldName)
		if len(positionToImpossibleFieldNames[i]) == 19:
			newLastPossibleField = fieldNameSet - positionToImpossibleFieldNames[i]
			remove(newLastPossibleField.pop(), i, positionToPossibleFieldNames, positionToImpossibleFieldNames, fieldNameSet, removedSet)

removedSet = set()

with open('day16.txt', 'r') as file:
	text = file.read().split('\n\n')


	validNumSetMap = {}
	validNumSet = set()
	for rule in text[0].split('\n'):
		fieldName = rule.split(':')[0]
		validNumSetMap[fieldName] = set()

		firstRange = rule.split(' or ')[0].split()[-1]
		secondRange = rule.split(' or ')[1].strip()
		min1, max1 = [int(x) for x in firstRange.split('-')]
		min2, max2 = [int(x) for x in secondRange.split('-')]
		for i in range(min1, max1 + 1):
			validNumSetMap[fieldName].add(i)
			validNumSet.add(i)
		for i in range(min2, max2 + 1):
			validNumSetMap[fieldName].add(i)
			validNumSet.add(i)


	sumOfInvailds = 0

	otherTickets = text[2].split('\n')[1:-1]

	positionToPossibleFieldNames = {}
	positionToImpossibleFieldNames = {}

	invalidTicketSet = set()
	for n, ticket in enumerate(otherTickets):
		fieldVals = [int(x) for x in ticket.strip().split(',')]
		for val in fieldVals:
			if val not in validNumSet:
				invalidTicketSet.add(n)

	print(invalidTicketSet)

	for n, ticket in enumerate(otherTickets):
		if n in invalidTicketSet:
			continue
		fieldVals = [int(x) for x in ticket.strip().split(',')]
		for j, val in enumerate(fieldVals):
			i = j + 1

			if i not in positionToImpossibleFieldNames:
				positionToImpossibleFieldNames[i] = set()
			if i not in positionToPossibleFieldNames:
				positionToPossibleFieldNames[i] = set()

			for fieldName in validNumSetMap:
				if i in positionToImpossibleFieldNames and fieldName in positionToImpossibleFieldNames[i]:
					continue
				elif val in validNumSetMap[fieldName]:
					positionToPossibleFieldNames[i].add(fieldName)
				else:
					positionToImpossibleFieldNames[i].add(fieldName)
					if fieldName in positionToPossibleFieldNames[i]:
						positionToPossibleFieldNames[i].remove(fieldName)

				if i in positionToImpossibleFieldNames and len(positionToImpossibleFieldNames[i]) == 19:
					lastPossibleField = validNumSetMap.keys() - positionToImpossibleFieldNames[i]
					remove(lastPossibleField.pop(), i, positionToPossibleFieldNames, positionToImpossibleFieldNames, validNumSetMap.keys(), removedSet)
					

	print(positionToPossibleFieldNames)
	# print(positionToImpossibleFieldNames)

	departurePositions = set()
	for position in positionToPossibleFieldNames:
		if positionToPossibleFieldNames[position].pop()[:len('departure')] == 'departure':
			departurePositions.add(position)

	print(departurePositions)
	product = 1
	for j, val in enumerate(text[1].split('\n')[1].split(',')):
		i = j + 1
		print(i, val)
		if i in departurePositions:
			product *= int(val)

	print(product)

