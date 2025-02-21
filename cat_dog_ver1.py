#!/usr/bin/env python3

# Source: https://codingbat.com/prob/p164876
# Task: Return True if the string "cat" and "dog" appear the same number of times in the given string.
# Example output: 
#		cat_dog('catdog') → True
#		cat_dog('catcat') → False
#		cat_dog('1cat1cadodog') → True

def cat_dog(str):
  word_1 = "cat"
  word_2 = "dog"
  index = 0
  counter_1 = 0
  counter_2 = 0
  
  while index < len(str) - 2:
    if str[index:index + 3] == word_1:
      counter_1 += 1
    if str[index:index + 3] == word_2:
      counter_2 += 1
    index += 1
  return counter_1 == counter_2

# Tests:
print(cat_dog('catdog') == True)
print(cat_dog('catcat') == False)
print(cat_dog('1cat1cadodog') == True)
print(cat_dog('catxxdogxxxdog') == False)
print(cat_dog('catxdogxdogxcat') == True)
print(cat_dog('catxdogxdogxca') == False)
print(cat_dog('dogdogcat') == False)
print(cat_dog('dogogcat') == True)
print(cat_dog('dog') == False)
print(cat_dog('cat') == False)
print(cat_dog('ca') == True)
print(cat_dog('c') == True)
print(cat_dog('') == True)
