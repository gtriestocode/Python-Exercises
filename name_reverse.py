#!/usr/bin/env python3

# Task: Print the name of the user in reverse.
# Example input: Harold
# Example output: dloraH

name = input("What's your name? ")
index = len(name) - 1
reverse_name = ""

while index >= 0:
	reverse_name = reverse_name + name[index]  
	index = index - 1

print(reverse_name)
