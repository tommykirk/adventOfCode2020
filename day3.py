

currCol = 0
trees = 0

with open('day3.txt', 'r') as file:
	skiMap = [[c for c in line[:-1]] for line in file]
	rowLen = len(skiMap[0])
	for line in skiMap[1:]:
		currCol += 3
		currCol = currCol % rowLen
		if line[currCol] == '#':
			trees += 1
print(trees)