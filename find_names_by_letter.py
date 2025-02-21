#!/usr/bin/env python3

# Task: Find all the names that start with the user given letter.
# Example input: "m"
# Example output:
#		Matthew
#		Miranda

my_name_list = ["Alfred", "Anika", "Boris", "Jack", "Harley", "Matthew", "Miranda", "Dorian"]
index = 0
letter = input("Enter any letter: ").lower()

while index < len(my_name_list):
	name = my_name_list[index].lower()
	if name[0] == letter:
		print(my_name_list[index])
	index = index + 1
