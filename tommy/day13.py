


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

