#!/usr/bin/env python3

# Task: Convert a user comma separated text of numbers to a regular text
# Example Input: "97,98,99"
# Example Output: "abc"

numbers_text = input("Enter the numbers to convert: ") + "," 
index = 0
previous_comma_index = -1
output_text = ""
comma = ","

while index < len(numbers_text):
	if numbers_text[index] == comma:
		number = int(numbers_text[previous_comma_index + 1:index])
		letter = chr(number)
		output_text += letter
		previous_comma_index = index	
	index += 1

print(output_text)
