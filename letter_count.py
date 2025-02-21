#!/usr/bin/env python3

# Task: Count a letter in the given string.
# Example input: letter = "s"
# Example output: 18

lorem_ipsum_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
letter = input("Please enter the letter you want to count: ")
index = 0
result = 0

while index < len(lorem_ipsum_text):
	letter_to_check = lorem_ipsum_text[index]
	if letter_to_check == letter:
		result = result + 1
	index = index + 1

print(result)
