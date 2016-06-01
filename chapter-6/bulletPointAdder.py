#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip
text = pyperclip.paste()
lines = text.split('\n')
for line in range(len(lines)):
	lines[line] = '* ' + lines[line]
pyperclip.copy('\n'.join(lines))

