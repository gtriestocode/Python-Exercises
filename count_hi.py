#!/usr/bin/env python3

# Source: https://codingbat.com/prob/p167246
# Task: Return the number of times that the string "hi" appears anywhere in the given string.
# Example output:
#		count_hi('abc hi ho') → 1
#		count_hi('ABChi hi') → 2
#		count_hi('hihi') → 2

def count_hi(str):
  index = 0
  result = 0
  word_str = "hi"
  
  while index < len(str) - 1:
    if str[index:index + 2] == word_str:
      result += 1
    index += 1
  
  return result

# Tests: 
print(count_hi('abc hi ho') == 1)
print(count_hi('ABChi hi') == 2)
print(count_hi('hihi') == 2)	
print(count_hi('hiHIhi') == 2)	
print(count_hi('') == 0)	
print(count_hi('h') == 0)	
print(count_hi('hi') == 1)
print(count_hi('Hi is no HI on ahI') == 0)	
print(count_hi('hiho not HOHIhi') == 2)
