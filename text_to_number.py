#!/usr/bin/env python3

# Task: Convert a user regular text to a comma separated text of numbers, representing the characters of the text
# Hint: You can use the "ord()" function to get the numerical value of a character
# Example Input: "abc"
# Example Output: "97,98,99"

text = input("Enter the text to convert: ")
index = 0
output_text = ""

while index < len(text):
	letter_number = ord(text[index])
	if index > 0:
		output_text += ","
	output_text += str(letter_number) 
	index += 1
	
print(output_text)
