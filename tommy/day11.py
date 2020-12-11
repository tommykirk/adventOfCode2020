




# xxx
# x5x
# xxx
def getNumAdjacentPeople(r, c, matrix):
	numAdjacentPeople = 0
	if r + 1 != len(matrix) and matrix[r+1][c] == '#':
		numAdjacentPeople += 1
	if r + 1 != len(matrix) and c + 1 != len(matrix[0]) and matrix[r+1][c+1] == '#':
		numAdjacentPeople += 1
	if r != 0 and matrix[r-1][c] == '#':
		numAdjacentPeople += 1
	if r != 0 and c != 0 and matrix[r-1][c-1] == '#':
		numAdjacentPeople += 1

	if c + 1 != len(matrix[0]) and matrix[r][c+1] == '#':
		numAdjacentPeople += 1
	if r != 0 and c + 1 != len(matrix[0]) and matrix[r-1][c+1] == '#':
		numAdjacentPeople += 1
	if c != 0 and matrix[r][c-1] == '#':
		numAdjacentPeople += 1
	if c != 0 and r + 1 != len(matrix) and matrix[r+1][c-1] == '#':
		numAdjacentPeople += 1

	return numAdjacentPeople

def getNumVisiblePeople(r, c, matrix):
	numAdjacentPeople = 0
	if getFirstNonEmptySquareInDirection(r, c, 1, 0, matrix) == '#':
		numAdjacentPeople += 1
	if getFirstNonEmptySquareInDirection(r, c, 1, 1, matrix) == '#':
		numAdjacentPeople += 1
	if getFirstNonEmptySquareInDirection(r, c, -1, 0, matrix) == '#':
		numAdjacentPeople += 1
	if getFirstNonEmptySquareInDirection(r, c, -1, -1, matrix) == '#':
		numAdjacentPeople += 1

	if getFirstNonEmptySquareInDirection(r, c, 0, 1, matrix) == '#':
		numAdjacentPeople += 1
	if getFirstNonEmptySquareInDirection(r, c, -1, 1, matrix) == '#':
		numAdjacentPeople += 1
	if getFirstNonEmptySquareInDirection(r, c, 0, -1, matrix) == '#':
		numAdjacentPeople += 1
	if getFirstNonEmptySquareInDirection(r, c, 1, -1, matrix) == '#':
		numAdjacentPeople += 1

	return numAdjacentPeople

def getFirstNonEmptySquareInDirection(r, c, rowDir, colDir, matrix):
	r += rowDir
	c += colDir
	while r < len(matrix) and c < len(matrix[0]) and r >= 0 and c >= 0:
		if matrix[r][c] != '.':
			return matrix[r][c]
		r += rowDir
		c += colDir
	return '.'

def compareTwoMatrices(originalSeatLayout, nextSeatLayout):
	for i in range(len(originalSeatLayout)):
		for j in range(len(originalSeatLayout[0])):
			if originalSeatLayout[i][j] != nextSeatLayout[i][j]:
				return False
	return True


with open('day11.txt', 'r') as file:
	numComps = 0
	replacementSeatMatrix = [[c for c in line.strip()] for line in file]
	# print(replacementSeatMatrix)
	seatMatrix = [['0' for x in seatMatrixRow] for seatMatrixRow in replacementSeatMatrix]

	while not compareTwoMatrices(seatMatrix, replacementSeatMatrix) and numComps < 100:
		numComps += 1

		replacementSeatMatrix, seatMatrix = seatMatrix, replacementSeatMatrix	

		for r in range(len(seatMatrix)):
			for c in range(len(seatMatrix[0])):
				if seatMatrix[r][c] == '.':
					replacementSeatMatrix[r][c] = '.'
				elif seatMatrix[r][c] == '#': 
					if getNumVisiblePeople(r, c, seatMatrix) >= 5:
						replacementSeatMatrix[r][c] = 'L'
					else:
						replacementSeatMatrix[r][c] = '#'
				else:
					if getNumVisiblePeople(r, c, seatMatrix) > 0:
						replacementSeatMatrix[r][c] = 'L'
					else:
						replacementSeatMatrix[r][c] = '#'

	print('numComps: ', numComps)
	# print(replacementSeatMatrix)

	count = 0

	for r in range(len(seatMatrix)):
		for c in range(len(seatMatrix[0])):
			if replacementSeatMatrix[r][c] == '#':
				count += 1
	print(count)


