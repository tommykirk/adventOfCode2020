


inputList = [int(n) for n in '9,12,1,4,17,0,18'.split(',')]
# inputList = [int(n) for n in '2, 1, 3'.split(',')]
numberToMostRecentIndexMap = {}


for i, n in enumerate(inputList[:-1]):
	numberToMostRecentIndexMap[n] = i

prevNumSpoken = inputList[-1]
currNumSpoken = -1

for i in range(len(inputList), 30000000):
	if prevNumSpoken in numberToMostRecentIndexMap.keys():
		currNumSpoken = i - 1 - numberToMostRecentIndexMap[prevNumSpoken]
		numberToMostRecentIndexMap[prevNumSpoken] = i - 1
		prevNumSpoken = currNumSpoken
	else:
		numberToMostRecentIndexMap[prevNumSpoken] = i - 1
		prevNumSpoken = 0

	if i % 1000000 == 0:
		print(i, prevNumSpoken)
	if i == 29999999:
		# print(numberToMostRecentIndexMap)
		print(prevNumSpoken)

# print(numberToMostRecentIndexMap)




