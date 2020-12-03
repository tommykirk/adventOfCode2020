

currCol = 0
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
trees = []

with open('day3.txt', 'r') as file:
	skiMap = [[c for c in line[:-1]] for line in file]
	rowLen = len(skiMap[0])

	for slope in slopes:
		row = slope[0]
		col = slope[1]
		currRow = row
		currCol = col
		numTrees = 0
		while currRow < len(skiMap):
			currCol = currCol % rowLen
			if skiMap[currRow][currCol] == '#':
				numTrees += 1
			currRow += row
			currCol += col
		trees += [numTrees]
print(trees)
i = 1
for t in trees:
	i *= t
print(i)
