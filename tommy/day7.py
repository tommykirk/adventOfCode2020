import re

# shiny plum bags contain no other bags.
# clear crimson bags contain 3 pale aqua bags, 4 plaid magenta bags, 3 dotted beige bags, 3 dotted black bags.

SPECIAL_BAG = 'shiny gold'

class Day7:

	bagToBagContents = {}
	bagToBagParents = {}

	def __init__(self):
		self.constructMaps()

	def main(self):
		# print(self.bagToBagContents)
		print(self.getShinyGoldAncestorsSize())
		print(self.getBagsInShinyGoldBag())


	def constructMaps(self):

		with open('day7.txt', 'r') as file:
			for rule in file:
				parentBag = rule.split(' bags')[0]
				if not re.search('no other bags.', rule):
					containingBags = rule[:-1].split('contain ')[1].split(', ')
					self.bagToBagContents[parentBag] = set((bag.split()[1] + ' ' + bag.split()[2], int(bag.split()[0])) for bag in containingBags)
					for containingBagTuple in self.bagToBagContents[parentBag]:
						containingBag = containingBagTuple[0]
						if containingBag not in self.bagToBagParents.keys():
							self.bagToBagParents[containingBag] = set()
						self.bagToBagParents[containingBag].add(parentBag)

	def getBagsInShinyGoldBag(self):
		return self.getNumberOfChildrenBags(SPECIAL_BAG)
			
	def getNumberOfChildrenBags(self, bagName):
		if bagName not in self.bagToBagContents.keys():
			return 0
		else:
			return sum((self.getNumberOfChildrenBags(childBagTuple[0]) + 1) * childBagTuple[1] for childBagTuple in self.bagToBagContents[bagName])

	def getShinyGoldAncestorsSize(self):				
		shinyGoldAncestors = set()
		visited = set()
		toVisit = [SPECIAL_BAG]
		while toVisit:
			nextToVisit = toVisit.pop()
			if nextToVisit in visited:
				continue
			shinyGoldAncestors.add(nextToVisit)
			visited.add(nextToVisit)
			if nextToVisit in self.bagToBagParents:
				toVisit += self.bagToBagParents[nextToVisit]

		return len(shinyGoldAncestors) - 1
		# print(bagToBagParents)
		# print(bagToBagParents)
		# print(shinyGoldAncestors)
		# print(len(shinyGoldAncestors) - 1)



day7 = Day7()
day7.main()
