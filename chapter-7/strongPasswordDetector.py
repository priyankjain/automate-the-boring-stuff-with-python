#! python3
# strongPasswordDetector.py - A regex-based python to determine 
# whether a password is strong
# A strong password is one that satisfies following conditions:
# - Length >= 8
# - Contains an uppercase character
# - Contains a lowercase character
# - Contains a digit
# Author: Priyank Jain
#################################################################
import re
password = input("Enter your password:\n")
strongPasswordRegex = re.compile('''^
(?=.*[a-z])
(?=.*[A-Z])
(?=.*[0-9]).+$''', re.VERBOSE)
match = strongPasswordRegex.search(password)
if match is None:
	print("Password should contain both uppercase and lowercase characters and atleast a digit, with minimum length of 8 characters")
else:
	print("Congratulations, your password is strong!")

