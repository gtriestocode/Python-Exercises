#!/usr/bin/env python3

# Source: https://codingbat.com/prob/p164876
# Task: Return True if the string "cat" and "dog" appear the same number of times in the given string.
# Example output: 
#		cat_dog('catdog') → True
#		cat_dog('catcat') → False
#		cat_dog('1cat1cadodog') → True
  
def cat_dog(str):
  cat_count = count_word(str, "cat")
  dog_count = count_word(str, "dog")
  return cat_count == dog_count
  
def count_word(str, word):
  index = 0
  word_count = 0
  
  while index <= len(str) - len(word):
    if str[index:index+len(word)] == word:
      word_count += 1
    index += 1

  return word_count

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
