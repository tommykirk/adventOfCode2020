# S3
# R90
# E1
# S3
# E5
# S4
# E5
# N3
# W1
# N3
# F91
# W1
# F49


#   (10, 1)    (-1, 10),    (-10, -1), (1, -10)

wayPoint = [10, 1]
with open('day12.txt', 'r') as file:
	currCoords = [0, 0]
	directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	currDirection = 0
	cardinals = {
		'E': directions[0],
		'N': directions[1],
		'W': directions[2],
		'S': directions[3]
	}
	for line in file:
		action = line[0]
		value = int(line[1:])
		if action in cardinals.keys():
			wayPoint[0] += value * cardinals[action][0]
			wayPoint[1] += value * cardinals[action][1]
		elif action == 'L':
			v = (value // 90) % 4
			for i in range(v):
				wayPoint[0], wayPoint[1] = wayPoint[1], wayPoint[0]
				wayPoint[0] *= -1
		elif action == 'R':
			v = (value // 90) % 4
			for i in range(v):
				wayPoint[0], wayPoint[1] = wayPoint[1], wayPoint[0]
				wayPoint[1] *= -1
		elif action == 'F':
			currCoords[0] += value * wayPoint[0]
			currCoords[1] += value * wayPoint[1]
		else:
			print('ERROR: ', line)

	print(currCoords)
	print(sum(abs(c) for c in currCoords))

