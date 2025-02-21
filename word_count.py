#!/usr/bin/env python3

# Task: Count the words from the given text
# Example input: Nothing
# Example output: 69

lorem_ipsum_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
index = 0
word_count = 0

while index < len(lorem_ipsum_text):
	letter = lorem_ipsum_text[index] 
	if letter == " ":
		word_count = word_count + 1
	index = index + 1

word_count = word_count + 1	
print(word_count)
