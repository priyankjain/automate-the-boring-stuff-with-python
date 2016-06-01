#! python3
# numberAndEmailExtractor.py - Python script to extract email and
# phone numbers from clipboard text and paste them back to the clipboard
# Author: Priyank Jain
import re, pyperclip
text = pyperclip.paste()
phoneRegex = re.compile('''(
	(\d{3}|\(\d{3}\))? # Area code
	(\s|\.|\-)? 	  # Seperator
	(\d{3})		  # Next three digits
	(\s|\.|\-)	  # Seperator
	(\d{4})		  # Next four digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE | re.I)
emailRegex = re.compile('''(
	[\w.%+-]+ # Part before @
	@              # Required @ symbol
	[\w.-]+    # Domain part
	(\.[a-zA-Z]{2,4})
)''', re.VERBOSE | re.I)
text = text.replace('\n','')
phoneMatches = phoneRegex.findall(text)
emailMatches = emailRegex.findall(text)
matches = []
for groups in phoneMatches:
	phoneNum = ''
	if groups[1] != '':
		phoneNum += groups[1] + '-'
	phoneNum += '-'.join([groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailMatches:
	matches.append(groups[0])
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found in clipboard text.')
