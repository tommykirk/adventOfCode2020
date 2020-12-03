
m = set()
pairMap = {}
with open('day1.txt', 'r') as file:
	for line in file:
		currNum = int(line)

		if 2020 - currNum in pairMap.keys():
			print(currNum * pairMap[2020-currNum][0] * pairMap[2020-currNum][1])
		else:
			for prevNum in m:
				pairMap[prevNum + currNum] = (prevNum, currNum)
			m.add(currNum)



