#!/usr/bin/env python3

# Task: Divide the number without using the division operator. Print the result and the remainder.
# Example input: divident = 18, divisor = 5
# Example output: 18 : 5 = 3, with the remainder of 3

divident = int(input("Enter the divident first: "))
divisor = int(input("Enter the divisor: "))
remainder = divident
counter = 0

while remainder >= divisor:
	 remainder = remainder - divisor
	 counter += 1
	 
print(str(divident) + " : " + str(divisor) + " = " + str(counter) + ", with the remainder of " + str(remainder))
