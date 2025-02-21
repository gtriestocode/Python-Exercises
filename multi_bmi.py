#!/usr/bin/env python3

# Task: Calculate and print all the BMIs of the given user data (lists).
# Example input: Nothing
# Example output: 
# 		Alfred's BMI is 25.64891761567662
# 		Pennywise's BMI is 17.99816345270891
# 		Boris's BMI is 28.254847645429365
# 		Gerald's BMI is 23.450918219051392
# 		Kim's BMI is 18.19548277362446
# 		Phillip's BMI is 21.75
# 		Frank's BMI is 23.589835468362743

name_list = ["Alfred", "Pennywise", "Boris", "Gerald", "Kim", "Phillip", "Frank"]
weight_list = [ 75, 49, 102, 71, 46, 87, 79 ]
height_list = [ 1.71, 1.65, 1.90, 1.74, 1.59, 2.00, 1.83 ]

index = 0

while index < len(weight_list) and index < len(height_list) and index < len(name_list):
	bmi = weight_list[index] / (height_list[index] ** 2)
	name = name_list[index]
	print(name + "'s BMI is " + str(bmi))
	index += 1
