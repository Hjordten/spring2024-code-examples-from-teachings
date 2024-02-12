# Ex: Sort a list
# Solution
#
# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
#
# Sort this list by using the sorted() build in function.
#
# Sort the list in reversed order.
#
# Sort the list on the lenght of the name.
#
# Sort the list based on the last letter in the name.
#
# Sort the list in a way that the names that has an ‘a’ in it should be sorted first (still alphabetically).

l = ['Claus', 'Ib', 'Per']

sorted_list = sorted(l)

reversed_list = sorted(l, reverse=True)

sorted_by_length = sorted(l, key=len)

sorted_by_last_letter = sorted(l, key=lambda x: x[-1])

sorted_with_a_first = sorted(l, key=lambda x: (not 'a' in x, x))
