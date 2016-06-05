#! python3
# removeCsvHeader.py - Removes the header from all CSV files
# in the current working directory
# Author: Priyank Jain
#####################################################################
import csv, os
os.makedirs('headerRemoved', exist_ok = True)

for csvFileName in os.listdir('.'):
	if not csvFileName.endswith('.csv'):
		continue
	print('Removing header from ' + csvFileName + '....')
	inputFile = open(csvFileName)
	csvReader = csv.reader(inputFile)
	outputFile = open(os.path.join('headerRemoved','headerRemoved_{0}'.format(csvFileName)),'w')
	outputWriter = csv.writer(outputFile)
	for row in csvReader:
		if csvReader.line_num == 1:
			continue
		outputWriter.writerow(row)
	inputFile.close()
	outputFile.close()


