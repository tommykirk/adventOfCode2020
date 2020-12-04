import re


requiredFields = {
	'byr': lambda val: int(val) >= 1920 and int(val) <= 2002, 
	'iyr': lambda val: int(val) >= 2010 and int(val) <= 2020, 
	'eyr': lambda val: int(val) >= 2020 and int(val) <= 2030, 
	'hgt': lambda val: hgtCheck(val), 
	'hcl': lambda val: re.match('#[0-9a-f]{6}$', val), 
	'ecl': lambda val: val in eyeColors, 
	'pid': lambda val: re.match('[0-9]{9}$', val)
	}
eyeColors = set(['amb','blu','brn','gry','grn','hzl','oth'])
optionalFields = ('cid')

def main():

	validPassportCount = 0

	with open('day4.txt', 'r') as file:
		fileString = file.read()
		passportStrings = fileString.split('\n\n')
		for passportString in passportStrings:
			kvPairs = passportString.split()
			keys = set(kvPair.split(':')[0] for kvPair in kvPairs)
			if len(keys) < 7:
				continue
			missingKeys = requiredFields.keys() - keys
			if len(missingKeys) == 0:
				if validateValues(kvPairs):
					validPassportCount += 1

	print(validPassportCount)


def validateValues(kvPairs):
	for kvPair in kvPairs:
		key, value = kvPair.split(':')[0], kvPair.split(':')[1]
		if key in requiredFields.keys():
			if requiredFields[key](value):
				continue
			else:
				return False
	return True

def hgtCheck(val):
	if val[-2:] == 'in':
		return int(val[:-2]) >= 59 and int(val[:-2]) <= 76
	if val[-2:] == 'cm':
		return int(val[:-2]) >= 150 and int(val[:-2]) <= 193
	return False

if __name__ == '__main__':
	main()


