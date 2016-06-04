#! python3
# blankRowInserter.py - Insert n blanks rows starting from mth row
# Author: Priyank Jain
#####################################################################
import sys, openpyxl, os
if len(sys.argv)<4:
	print('Usage: python3 blankRowInserter.py m n excelFilePath')
	sys.exit(-1)
m = None
n = None
excelFilePath = None
try:
	m = int(sys.argv[1])
	n = int(sys.argv[2])
	excelFilePath = sys.argv[3]
except ValueError as e:
	print('Both m and n should be integers')
	sys.exit(-2)
if not os.path.exists(excelFilePath):
	print('The specified file does not exist')
	sys.exit(-3)
inputWb = openpyxl.load_workbook(excelFilePath)
inputSheet = inputWb.active
outputWb = openpyxl.Workbook()
outputSheet = outputWb.active
for rowNum in range(1, inputSheet.max_row+1):
	for colNum in range(1, inputSheet.max_column + 1):
		if rowNum<m:
			outputSheet.cell(row=rowNum, column=colNum).value = inputSheet.cell(row=rowNum, column=colNum).value
		else:
			outputSheet.cell(row=rowNum+n, column=colNum).value = inputSheet.cell(row=rowNum, column=colNum).value
fileName, fileExtension = os.path.splitext(excelFilePath)
outputWb.save('{0}_with_blanks{1}'.format(fileName, fileExtension))
inputWb.save(excelFilePath)
