

def part1(changedIndex):
	global instructions
	global visitedIndices
	visitedIndices = set()
	with open('day8.txt', 'r') as file:
		instructions = [(line.split()[0], line.split()[1]) for line in file]
		currIndex = 0
		acc = 0
		while currIndex not in visitedIndices and currIndex < len(instructions):
			operation, argument = instructions[currIndex][0], instructions[currIndex][1]

			if currIndex == changedIndex:
				if operation == 'nop':
					operation = 'jmp'
				elif operation == 'jmp':
					operation = 'nop'

			visitedIndices.add(currIndex)
			if operation == 'acc':
				acc += int(argument)
				currIndex += 1
			elif operation == 'jmp' :
				currIndex += int(argument)
			elif operation == 'nop':
				currIndex += 1
			else:
				print('ERROR: invalid operation')
				break

		# if currIndex == len(instructions):
		# 	print(changedIndex)
		return currIndex == len(instructions), acc

part1(-1)

for index in visitedIndices:
	if instructions[index][0] == 'acc':
		continue
	else:
		if part1(index)[0]:
			print(part1(index)[1])

