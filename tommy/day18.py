# 5 * (2 * 8) * 6 + 4
# 5 * (5 + 2 * 7) * 5



# (6 * (2 * 7 * 3 * 7 * 2) + 5 * 4 + (2 * 9 + 8 + 3) + 6) * (8 + 3 * 9) * ((9 * 2) + 2)

def parse(parseList):
	if len(parseList) < 3:
		return
	elif  '(' in parseList[-3:]:
		return
	else:
		num2 = parseList.pop()
		op = parseList.pop()
		if op == '*':
			parseList[-1] *= num2
		else:
			parseList[-1] += num2


# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
with open('day18.txt', 'r') as file:
	sumOfLines = 0
	i = 0
	for line in file:
		i += 1
		parseList = []
		for c in line.strip().replace(' ',''):
			print(parseList, c)
			if c != ')':
				if c not in ['(','*','+']:
					parseList.append(int(c))
					if len(parseList) >= 2 and parseList[-2] == '+':
						parse(parseList)
				else:
					parseList.append(c)
			else:
				while len(parseList) >= 3 and '(' not in parseList[-3:]:
					parse(parseList)
				parseList[-2] = parseList[-1]
				parseList.pop()
				while len(parseList) >= 3 and '(' not in parseList[-3:] and parseList[-2] == '+':
					parse(parseList)

		print(i)
		while len(parseList) > 1:
			parse(parseList)
		sumOfLines += parseList[0]

		print(sumOfLines)
