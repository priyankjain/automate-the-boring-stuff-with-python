#! python3
# mcp.pyw - A multiclipboard project. Usage:
# python3 mpc.pyw save google # Stores the current clipboard content with the tag google
# python3 mpc.pyw google      # Copies the text under tag google to the clipboard
# python3 mpc.pyw list        # Lists all the tags and the text stored
# under them in the multi-clipboard
# Author: Priyank Jain
#####################################################################
import shelve, pyperclip, sys, os
if len(sys.argv) < 2 or (sys.argv[1] == 'save' and (len(sys.argv) < 3 or sys.argv[2]=='' or sys.argv[2]==' ')):
	print("""Usage:
python3 mpc.pyw save <tag> # Stores the current clipboard content with the specified tag
python3 mpc.pyw <tag>      # Copies the text under the specified tag to the clipboard
python3 mpc.pyw list       # List all the tags and corresponding text stored
""")
	sys.exit(-1)

shelfFile = None
shelfFile = shelve.open('clipboard')

try:
	if sys.argv[1] == "list":
		if len(shelfFile) > 0:
			for key, value in shelfFile.items():
				print('{0} -> {1}\n'.format(key, value))
		else:
			print("No content saved to multiclipboard yet")
	elif sys.argv[1] == "save":
		text = pyperclip.paste()
		shelfFile[sys.argv[2]] = text
		print("Clipboard content successfull saved under tag {0}".format(sys.argv[2]))
	elif sys.argv[1] in shelfFile:
		pyperclip.copy(shelfFile[sys.argv[1]])
		print("Content under tag {0} successfully copied to clipboard".format(sys.argv[1]))
	else:
		print("No tag found with name {0}".format(sys.argv[1]))
except IndexError as e:
	print(e.stacktrace())
finally:
	shelfFile.close()
