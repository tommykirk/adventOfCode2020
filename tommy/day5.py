


def main():
	seatsSet = set()
	maxSeatId = 0
	with open('day5.txt', 'r') as file:
		for boardingPass in file:
			nextSeatId = boardingPassToSeatID(boardingPass)
			maxSeatId = max(maxSeatId, nextSeatId)
			seatsSet.add(nextSeatId)
		for seat in range(128 * 8):
			if seat not in seatsSet and seat-1 in seatsSet and seat+1 in seatsSet:
				print("part2: " + str(seat))

	print("part1: " + str(maxSeatId))




def boardingPassToSeatID(boardingPass):
	boardingPass = boardingPass.replace('B', '1')
	boardingPass = boardingPass.replace('F', '0')

	row = int(boardingPass[:-4], 2)
	boardingPass = boardingPass.replace('L','0')
	boardingPass = boardingPass.replace('R','1')
	col = int(boardingPass[-4:], 2)
	return row * 8 + col

if __name__ == '__main__':
	main()