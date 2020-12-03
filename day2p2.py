

validPasswordCount = 0

with open('day2.txt', 'r') as file:
	for line in file:
		words = line.split(' ')
		charSlots = [int(num) for num in words[0].split('-')]
		char = words[1][0]
		password = words[2]
		firstSlotIsChar = password[charSlots[0]-1] == char
		secondSlotIsChar = password[charSlots[1]-1] == char
		if firstSlotIsChar ^ secondSlotIsChar:
			validPasswordCount+=1


print(validPasswordCount)


