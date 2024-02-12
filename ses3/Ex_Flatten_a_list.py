# Flatten this list (using a list comprehension):
# 
# list_of_lists = [
#     [1, 2, 3],
#     [4, 5],
#     [6],
#     [7, 8, 9],
# ]
# So it becomes like this:
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_lists = [
    [1,  2,  3],
    [4,  5],
    [6],
    [7,  8,  9],
]

flat_list = [item for sublist in list_of_lists for item in sublist]

print(flat_list)
