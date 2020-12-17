
def main():

	tupleMap = {}
	with open('day17.txt', 'r') as file:

		w = 0
		y = 0
		z = 0
		for line in file:
			for x, val in enumerate(line.strip()):
				tupleMap[(w, x, y, z)] = 1 if val == '#' else 0
			y += 1

		for _ in range(6):
			print('on step: ', _)
			iterate(tupleMap)

		print(tupleMap)

		active = 0
		for key in tupleMap:
			active += tupleMap[key]
		print('part2: ', active)




def iterate(tupleMap):
	wdiff = [-1, 0, 1]
	xdiff = [-1, 0, 1]
	ydiff = [-1, 0, 1]
	zdiff = [-1, 0, 1]

	nextIter = {}
	for w in range(-8, 15):
		for x in range(-8, 15):
			for y in range(-8, 15):
				for z in range(-8, 15):
					currTuple = (w, x, y, z)
					neighbors = 0
					for dw in wdiff:
						for dx in xdiff:
							for dy in ydiff:
								for dz in zdiff:
									if 0 == dx == dy == dz == dw:
										continue
									currNeighbor = (w + dw, x + dx, y + dy, z + dz)
									if tupleMap.get(currNeighbor, 0) == 1:
										neighbors += 1

					if tupleMap.get(currTuple, 0) == 1:
						if neighbors == 2 or neighbors == 3:
							continue
						else:
							nextIter[currTuple] = 0
					else:
						if neighbors == 3:
							nextIter[currTuple] = 1

	for key in nextIter:
		tupleMap[key] = nextIter[key]


main()


