#! python3
# tablePrinter.py - A function to pretty print a nested list
# Author: Priyank Jain
tableData = [['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose']]

def printTable(nestedList):
	maxColumnLength = []
	for innerList in nestedList:
		maxColumnLength.append(max(map(len, innerList)))
	if nestedList and len(nestedList) > 0:
		for rowNum in range(len(nestedList[0])):
			for colNum in range(len(nestedList)):
				print(nestedList[colNum][rowNum].rjust(maxColumnLength[colNum]),end = ' ')
			print()

printTable(tableData)
