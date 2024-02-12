# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # first we check if the string is at least length of 3
  if len(s) >= 3:
    # check if it ends with ing
    if s.endswith('ing'):
      # we take the original string, and add ly to its end
      return s + 'ly'
    else:
      # we take the original string, and add ing to its end
      return s + 'ing'
  return s

       


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
 # first we check if not and bad exists in string
 if 'not' in s and 'bad' in s:
   # we find the index of not and bad
   not_index = s.index('not')
   bad_index = s.index('bad') + len('bad')
   if not_index < bad_index:
    not_bad_substring = s[not_index:bad_index]
    s = s.replace(not_bad_substring, 'good')
 return s      


  


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

# <object>[<number>:<number>] Accesses the elements from the first number, up to but not including, the second number
# <object>[:<number>] Retrieves all elements from the start of the object up to, but not including, the specified index.
# <object>[<number>:] Retrieves all elements from the specified index to the end of the object.
# <object>[<number>] Accesses the element at the specified index position in the object.

def front_back(a, b):
  # First we check if the length of string a is odd
  if len(a) % 2 != 0:
   # we get the front of string a, remember to get the extra letter
   a_front = a[:(len(a) // 2) + 1]
   # we get the back of string a, remember to get the extra letter
   a_back = a[(len(a) // 2) + 1:]
  # else 
  else:  
  # we get the front of string a, we dont need the extra letter, since the length is even
    a_front = a[:(len(a) // 2)]
  # we get the back of string a, we dont need the extra letter, since the length is even
    a_back = a[(len(a) // 2):]
  # we check if the length of string b is odd 
  if len(b) % 2 != 0:
  # we get the front of string b, remember to get the extra letter
    b_front = b[:(len(b) // 2) + 1]
  # we get the back of string b, remember to get the extra letter
    b_back = b[(len(b) // 2) + 1:]
  #else    
  else:  
  # we get the front of string b, we dont need the extra letter, since the length is even
     b_front = b[:(len(b) // 2)]
  # we get the back of string b, we dont need the extra letter, since the length is even
     b_back = b[(len(b) // 2):]
  # return a formatted string with the correct variables   
  return f'{a_front}{b_front}{a_back}{b_back}'

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print (prefix + ' got: ' + got + ' expected: ' + expected)


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

main()
