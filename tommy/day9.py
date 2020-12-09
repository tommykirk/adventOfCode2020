

with open('day9.txt', 'r') as file:
	lines = [int(line) for line in file]

def part1():
	prev25 = set(lines[:25])
	for i in range(25, len(lines)):
		curr = lines[i]
		hasPairThatSums = False
		for v in prev25:
			if curr - v != v and curr - v in prev25:
				hasPairThatSums = True
				break
		if not hasPairThatSums:
			return curr
		prev25.remove(lines[i - 25])
		prev25.add(curr)
	return 0

def part2(target):
	cumSums = [0] * len(lines)
	currSum = 0
	for i, val in enumerate(lines):
		cumSums[i] = currSum + val
		currSum += val

	prevSums = {}

	for i, currSum in enumerate(cumSums):
		if currSum - target in prevSums.keys():
			return min(lines[prevSums[currSum - target] + 1:i + 1]) + max(lines[prevSums[currSum - target] + 1:i + 1])
		else:
			prevSums[currSum] = i
	return 0


target = part1()
print(part1())
print(part2(target))




