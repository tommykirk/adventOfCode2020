import re

# shiny plum bags contain no other bags.
# clear crimson bags contain 3 pale aqua bags, 4 plaid magenta bags, 3 dotted beige bags, 3 dotted black bags.

def main():
	bagToBagContents = {}
	bagToBagParents = {}

	with open('day7.txt', 'r') as file:
		for rule in file:
			parentBag = rule.split(' bags')[0]
			if not re.search('no other bags.', rule):
				if parentBag in bagToBagContents.keys():
					bagToBagContents[parentBag] += set((bag.split()[0] + ' ' + bag.split()[1]) for bag in re.split('[1-9]+ ', rule)[1:])
				else:
					bagToBagContents[parentBag] = set((bag.split()[0] + ' ' + bag.split()[1]) for bag in re.split('[1-9]+ ', rule)[1:])
				for containingBag in bagToBagContents[parentBag]:
					if containingBag not in bagToBagParents.keys():
						bagToBagParents[containingBag] = set()
					bagToBagParents[containingBag].add(parentBag)
					
	shinyGoldAncestors = set()
	visited = set()
	toVisit = ['shiny gold']
	while toVisit:
		nextToVisit = toVisit.pop()
		if nextToVisit in visited:
			print('loop!')
			continue
		shinyGoldAncestors.add(nextToVisit)
		visited.add(nextToVisit)
		if nextToVisit in bagToBagParents:
			toVisit += bagToBagParents[nextToVisit]

	print(shinyGoldAncestors)
	print(len(shinyGoldAncestors) - 1)






main()
