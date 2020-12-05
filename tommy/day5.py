


def main():
	maxSeatId = 0
	with open('day5.txt', 'r') as file:
		for boardingPass in file:
			maxSeatId = max(maxSeatId, boardingPassToSeatID(boardingPass))
	print(maxSeatId)




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