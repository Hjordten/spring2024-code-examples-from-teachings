# Ex: Text editor plugin simulation
# Solution
#
# s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'
# Count the number of characters including blank spaces.
#
# Count the number of characters excluding blank spaces.
#
# Count the number of words.

s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

# Count the number of characters including blank spaces
total_chars = len(s)

# Count the number of characters excluding blank spaces
non_blank_chars = sum(1 for char in s if char != ' ')

# Count the number of words
words = len(s.split())

# Count the number of lines
lines = s.count('\n') +  1

print(f"Total characters (including spaces): {total_chars}")
print(f"Total characters (excluding spaces): {non_blank_chars}")
print(f"Total words: {words}")
print(f"Total lines: {lines}")
