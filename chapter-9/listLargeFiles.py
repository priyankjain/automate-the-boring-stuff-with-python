#! python3
# listLargeFiles.py - A program to list files that take up 
# more than 100 MB of disk spac
# Author: Priyank Jain
#####################################################################
import os
rootDir = '/'
for folderName, subFolders, fileNames in os.walk(rootDir):
	for fileName in fileNames:
		filePath = os.path.join(folderName, fileName)
		if os.path.exists(filePath):
			fileSize = os.path.getsize(filePath)
			fileSize = fileSize/1024/1024 # Convert it to MB
			if fileSize > 100:
				print("{0}\t{1}".format(fileSize,filePath))
