#! python3
# selectiveCopy.py - Selectively copy all jpg and pdf files in a
# folder to another folder
################################################################
import shutil, os
sourceFolder = input("Enter folder to be backed up:\n")
destFolder = input("Enter backup folder location:\n")
if not os.path.exists(sourceFolder) or not os.path.exists(destFolder):
	print("Please ensure that both the folder to backup and the backup folder exist")
	sys.exit(-1)

for folderName, subFolders, fileNames in os.walk(sourceFolder):
	print("Scanning folder {0}".format(folderName))
	for fileName in fileNames:
		if fileName.endswith(".pdf") or fileName.endswith(".jpg"):
			print("Making backup of {0}".format(fileName))
			filePath = os.path.join(folderName, fileName)
			shutil.copy(filePath, destFolder)
print("Successfully backed up jpg and pdf files in folder {0}".format(sourceFolder))
		
