
def main():

	tupleMap = {}
	with open('day17.txt', 'r') as file:

		y = 0
		z = 0
		for line in file:
			for x, val in enumerate(line.strip()):
				tupleMap[(x, y, z)] = 1 if val == '#' else 0
			y += 1

		print(tupleMap)
		for _ in range(6):
			iterate(tupleMap)

		print(tupleMap)

		active = 0
		for key in tupleMap:
			active += tupleMap[key]
		print('part1: ', active)




def iterate(tupleMap):
	xdiff = [-1, 0, 1]
	ydiff = [-1, 0, 1]
	zdiff = [-1, 0, 1]

	nextIter = {}
	for x in range(-10, 24):
		for y in range(-10, 24):
			for z in range(-10, 24):
				currTuple = (x, y, z)
				neighbors = 0
				for dx in xdiff:
					for dy in ydiff:
						for dz in zdiff:
							if 0 == dx == dy == dz:
								continue
							currNeighbor = (x + dx, y + dy, z + dz)
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


