#! python3
# regexStrip.py - A regex version of strip() function provided by the
# string class of Python
# strip() function removes any space character from the start and end 
# of a string
# Tab, newline, space are considered to be space characters
# Author: Priyank Jain
#####################################################################
import re

def strip(inputString):
	stripRegex = re.compile(r'(^\s*|\s*$)')
	return stripRegex.sub('',inputString)	
inputString = "\n\t Strip version\n "
print("String before calling strip():\n", inputString)
print("String after calling regex strip():", strip(inputString))
print("String after calling string's strip():", inputString.strip())
if strip(inputString) == inputString.strip():
	print("Yes, regex strip works the same way as the in-built \
strip function")
else:
	print("Oops, regex strip works differently than the \
in-built strip function")

