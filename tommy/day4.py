

requiredFields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
optionalFields = ('cid')

validPassportCount = 0

with open('day4.txt', 'r') as file:
	fileString = file.read()
	passportStrings = fileString.split('\n\n')
	for passportString in passportStrings:
		kvPairs = passportString.replace('\n', ' ').split(' ')
		keys = set(kvPair.split(':')[0] for kvPair in kvPairs)
		if len(keys) < 7:
			continue
		missingKeys = requiredFields - keys
		if len(missingKeys) == 0 or (len(missingKeys) == 1 and 'cid' in missingKeys):
			validPassportCount += 1

print(validPassportCount)

