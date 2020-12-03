

validPasswordCount = 0

with open('day2.txt', 'r') as file:
	for line in file:
		words = line.split(' ')
		minAndMax = [int(num) for num in words[0].split('-')]
		char = words[1][0]
		occurences = words[2].count(char)
		if occurences >= minAndMax[0] and occurences <= minAndMax[1]:
			validPasswordCount += 1


print(validPasswordCount)


