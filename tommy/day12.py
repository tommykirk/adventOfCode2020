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
			currCoords[0] += value * cardinals[action][0]
			currCoords[1] += value * cardinals[action][1]
		elif action == 'L':
			currDirection = (currDirection + (value // 90)) % 4
		elif action == 'R':
			currDirection = (currDirection - (value // 90)) % 4
		elif action == 'F':
			currCoords[0] += value * directions[currDirection][0]
			currCoords[1] += value * directions[currDirection][1]
		else:
			print('ERROR: ', line)

	print(currCoords)
	print(sum(abs(c) for c in currCoords))

