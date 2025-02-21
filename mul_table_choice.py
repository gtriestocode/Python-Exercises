#!/usr/bin/env python3

# Task: Print the multiplication table of the user given number.
# Example input: 4.5
# Example output: 
# 		4.5 x 1 = 4.5
# 		4.5 x 2 = 9.0
# 		4.5 x 3 = 13.5
# 		4.5 x 4 = 18.0
# 		4.5 x 5 = 22.5
# 		4.5 x 6 = 27.0
# 		4.5 x 7 = 31.5
# 		4.5 x 8 = 36.0
# 		4.5 x 9 = 40.5
# 		4.5 x 10 = 45.0

multi_num = float(input("Which number would you like to multiply? "))
counter = 1

while counter <= 10:
	result = multi_num * counter
	print(str(multi_num) + " x " + str(counter) + " = " + str(result))
	counter = counter + 1
