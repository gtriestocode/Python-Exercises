#!/usr/bin/env python3

# Task: Calculate the BMI of the user
# Example input: weight = 55, height = 1.69
# Example output: 19.257028815517668

weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))
bmi = weight / height ** 2 
print("Your BMI is " + str(bmi))
