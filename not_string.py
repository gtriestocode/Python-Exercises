#!/usr/bin/env python3

# Task: Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
# Example output:
#		not_string('candy') → 'not candy'
#		not_string('x') → 'not x'
#		not_string('not bad') → 'not bad'

def not_string(str):
	string = "not "
	if len(str) >= 3  and str[0] == "n" and str[1] == "o" and str[2] == "t":
		return str
	else:
		return string + str

print(not_string('candy') == 'not candy')
print(not_string('x') == 'not x')
print(not_string('not bad') == 'not bad')
print(not_string('bad') == 'not bad')
print(not_string('not') == 'not')	
print(not_string('is not') == 'not is not')
print(not_string('no') == 'not no')
