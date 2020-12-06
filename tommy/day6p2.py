

from functools import reduce


with open('day6.txt', 'r') as file:
	totalCount = 0
	groupSet = set()
	for customsFormGroup in file.read().split('\n\n'):
		customsFormGroupSet = reduce(lambda x, y : x.intersection(y), (set(line) for line in customsFormGroup.split()))
		# print(customsFormGroup)
		# print(customsFormGroupSet)
		totalCount += len(customsFormGroupSet)
	print(totalCount)

