#!/usr/bin/env python3

# Task: Check if the list contains a user defined number more than once.
# Example input: 9
# Example output: "This number has a duplicate"

num_list = [ 5, 9, 6, 9, 3, 2, 6, 6 ]
index = 0 
check_num = int(input("Enter the number to check: "))
count_num = 0

while index < len(num_list): 
	if check_num == num_list[index]:
		count_num += 1
	index += 1

if count_num > 1:
	print("This number has a duplicate")
else:
	print("No duplicates")
