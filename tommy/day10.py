


def part1(): 
	with open('day10.txt', 'r') as file:
		adapters = sorted([int(line) for line in file])
		prevVal = 0
		counts = [0] * 4
		for val in adapters:
			counts[val - prevVal] += 1
			prevVal = val
		counts[3] += 1

	print(counts)
	print(counts[1] * counts[3])




def part2():
	with open('day10.txt', 'r') as file:
		adapters = [0] + sorted([int(line) for line in file])

	waysToArrangeToEnd = [-1 for a in adapters]
	for i in range(len(waysToArrangeToEnd) - 1, -1, -1):
		if i == len(waysToArrangeToEnd) - 1:
			waysToArrangeToEnd[i] = 1
		else:
			curVal = adapters[i]
			waysToArrangeToEnd[i] = sum(waysToArrangeToEnd[i + j] for j in range(1, 4) if i + j < len(adapters) and adapters[i+j] - adapters[i] <= 3)
	print(adapters)
	print(waysToArrangeToEnd)


part2()