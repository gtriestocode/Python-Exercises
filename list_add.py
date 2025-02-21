#!/usr/bin/env python3

# Task: Add all the number in the given list.
# Example input: Nothing
# Example output: 470

my_list = [4, 5, 7, 9, 10, 15, 11, 409]
index = 0
result = 0

while index < len(my_list):
	result = result + my_list[index]
	index = index + 1

print(result)
