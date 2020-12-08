

def part1():
	visitedIndices = set()
	with open('day8.txt', 'r') as file:
		instructions = [line for line in file]
		currIndex = 0
		acc = 0
		while currIndex not in visitedIndices and currIndex < len(instructions):
			operation, argument = instructions[currIndex].split()

			visitedIndices.add(currIndex)
			if operation == 'acc':
				acc += int(argument)
				currIndex += 1
			elif operation == 'jmp':
				currIndex += int(argument)
			elif operation == 'nop':
				currIndex += 1
			else:
				print('ERROR: invalid operation')
				break

		print(currIndex)
		print(acc)



part1()
