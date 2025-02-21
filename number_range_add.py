#!/usr/bin/env python3

# Task: Add up all the numbers in the user given range.
# Example input: from_num = 5, to_num = 10 
# Example output: "Result: 45"

from_num = int(input("Enter the first number: "))
to_num = int(input("Enter the second number: "))

if from_num > to_num:
	temp = from_num
	from_num = to_num
	to_num = temp

counter = from_num
result = 0

while counter <= to_num:
	result = result + counter
	counter = counter + 1

print("Result: " + str(result))
