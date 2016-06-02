#! python3
# mapIt.py - A program to open google maps for a specific location
# Author: Priyank Jain
#####################################################################
import pyperclip, sys, webbrowser
address = ''
if len(sys.argv)>1: 
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()
if address!= '':
	webbrowser.open('https://www.google.com/maps/place/{0}'.\
format(address))

