#!/usr/bin/env python3

# Task: Find the average number of the given list of numbers. 
# Example input: Nothing
# Example output: 8.0

num = [4, 5, 7, 9, 10, 13]
index = 0 
add_num = 0

while index < len(num):
	add_num = add_num + num[index]
	index = index + 1
	
avg_num = float(add_num / len(num)) 
print(avg_num)

