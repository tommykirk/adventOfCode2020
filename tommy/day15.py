


inputList = [int(n) for n in '9,12,1,4,17,0,18'.split(',')]
# inputList = [int(n) for n in '2, 1, 3'.split(',')]
numberToMostRecentIndexMap = {}


for i, n in enumerate(inputList):
	numberToMostRecentIndexMap[n] = [i]

prevNumSpoken = inputList[-1]

for i in range(len(inputList), 30000000):
	if prevNumSpoken in numberToMostRecentIndexMap.keys() and len(numberToMostRecentIndexMap[prevNumSpoken]) == 2:
		prevNumSpoken = numberToMostRecentIndexMap[prevNumSpoken][1] - numberToMostRecentIndexMap[prevNumSpoken][0]
		if prevNumSpoken in numberToMostRecentIndexMap.keys():
			if len(numberToMostRecentIndexMap[prevNumSpoken]) == 2:
				numberToMostRecentIndexMap[prevNumSpoken][0] = numberToMostRecentIndexMap[prevNumSpoken][1]
				numberToMostRecentIndexMap[prevNumSpoken][1] = i
			else:
				numberToMostRecentIndexMap[prevNumSpoken] += [i]
		else:
			numberToMostRecentIndexMap[prevNumSpoken] = [i]
	else:
		if prevNumSpoken in numberToMostRecentIndexMap.keys() and len(numberToMostRecentIndexMap[prevNumSpoken]) == 1:
			prevNumSpoken = 0
			if prevNumSpoken in numberToMostRecentIndexMap.keys():
				if len(numberToMostRecentIndexMap[prevNumSpoken]) == 2:
					numberToMostRecentIndexMap[prevNumSpoken][0] = numberToMostRecentIndexMap[prevNumSpoken][1]
					numberToMostRecentIndexMap[prevNumSpoken][1] = i
				else:
					numberToMostRecentIndexMap[prevNumSpoken] += [i]
			else:
				numberToMostRecentIndexMap[prevNumSpoken] = [i]

	if i % 1000000 == 0:
		print(i, prevNumSpoken)
	if i == 29999999:
		# print(numberToMostRecentIndexMap)
		print(prevNumSpoken)

# print(numberToMostRecentIndexMap)




