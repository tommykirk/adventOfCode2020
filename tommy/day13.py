

def part1():
	with open('day13.txt', 'r') as file:
		arrivalTimestamp = int(file.readline())
		busIDs = file.readline().split(',')
		earliestBusTime = -1
		earliestBusID = -1


		for busID in busIDs:
			if busID == 'x':
				continue
			else:
				busInt = int(busID)
				candidateTime = busInt - (arrivalTimestamp % busInt)
				if candidateTime == busInt:
					candidateTime = 0
				if candidateTime < earliestBusTime or earliestBusTime == -1:
					earliestBusTime = candidateTime
					earliestBusID = busInt
		print(earliestBusID, earliestBusTime)
		print(earliestBusID * earliestBusTime)

#19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,859,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37


testInput = '67,7,59,61'

busIDs = testInput.split(',')
multOfEach = [0 for _ in range(len(busIDs))]
mult = 0
diff = 1
productOfPrevSeenPrimes = 1
while 67 * mult % 7 != 7 - diff:
	mult += productOfPrevSeenPrimes
print('67s: ', mult)
print(67 * mult)
currMult = int(((67 * mult) + diff) / 7)
print('7s: ', currMult)
print(7 * currMult)
print()
multOfEach[1] += currMult
multOfEach[0] += mult

diff += 1

productOfPrevSeenPrimes *= 7

while 67 * mult % 59 != 59 - diff:
	mult += productOfPrevSeenPrimes
	multOfEach[1] += (productOfPrevSeenPrimes  * 67 // 7)
	multOfEach[0] += productOfPrevSeenPrimes
print('67s: ', mult)
print(67 * mult)
currMult = int(((67 * mult) + diff) / 59)
print('59s: ', currMult)
print(59 * currMult)

multOfEach[2] = currMult

print(multOfEach)
print([multOfEach[i] * int(busIDs[i]) for i in range(len(busIDs))])

print()


def part2():
	with open('day13.txt', 'r') as file:
		file.readline()
		diffFromStart = -1
		mult = 0
		busIDs = [-1 if x == 'x' else int(x) for x in file.readline().split(',')]

		firstBus = busIDs[0]
		productOfPrevSeenPrimes = firstBus

		for i, busID in enumerate(busIDs):
			diffFromStart += 1
			if i == 0 or busID == -1:
				continue

			infbreak = 0
			while (firstBus * mult + diffFromStart) % busID != 0:
				mult += productOfPrevSeenPrimes // firstBus


			productOfPrevSeenPrimes *= busID

		print(mult * firstBus)
	

print('part2: ')
part2()
