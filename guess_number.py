#!/usr/bin/env python3

# Task: Ask the user to guess a secret predefined number.
# Example input: 52
# Example output: "Secret number is actually bigger than that"

sec_num = 95
num = int(input("What's the number? "))

if num < sec_num:
	print("Secret number is actually bigger than that")
elif num > sec_num:
	print("Secret number is actually smaller than that")
else:
	print("Bingo!")
