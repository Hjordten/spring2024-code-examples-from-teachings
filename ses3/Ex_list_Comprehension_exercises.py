# Ex: list Comprehension exercises
# Create a list of even numbers from 0 to 20.
#
# Create a list of squares of numbers from 1 to 10.
#
# Create a list of all the vowels in a given string.
#
# Create a list of common elements in two given lists. (could this be done with the use of another datastructure?)
#
# Create a list of words from a given string that have more than 4 and less than 8 letters.

even_numbers = [num for num in range(21) if num %  2 ==  0]

print(even_numbers)

squares = [num **  2 for num in range(1,  11)]

print(squares)

string = "Your example string goes here."
vowels = [char for char in string if char.lower() in 'aeiou']

print(vowels)

list1 = [1,  2,  3,  4,  5]
list2 = [4,  5,  6,  7,  8]
common_elements = [element for element in list1 if element in list2]

print(common_elements)

input_string = "Your input string goes here."
words = input_string.split()
selected_words = [word for word in words if  4 < len(word) <  8]

print(selected_words)