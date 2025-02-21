#!/usr/bin/env python3

# Task: Print all the multiplication table from 1 to 10.
# Example input: Nothing
# Example output: 
# 		1 x 1 = 1
# 		1 x 2 = 2
#		1 x 3 = 3
#   	...
#		10 x 8 = 80
# 		10 x 9 = 90
# 		10 x 10 = 100

multi_num = 1

while multi_num <= 10:
	counter = 1 
	while counter <= 10:
		result = multi_num * counter
		print(str(multi_num) + " x " + str(counter) + " = " + str(result))
		counter = counter + 1
	multi_num = multi_num + 1
