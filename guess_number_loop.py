#!/usr/bin/env python3

# Task: Ask the user to guess a secret predefined number until the user guesses correctly.
# Example input: 95
# Example output: "Bingo!"

sec_num = 95
num = 0

while num < sec_num or num > sec_num:
	num = int(input("What's the number? "))
	if num < sec_num:
		print("Secret number is actually bigger than that")
	elif num > sec_num:
		print("Secret number is actually smaller than that")

print("Bingo!")
