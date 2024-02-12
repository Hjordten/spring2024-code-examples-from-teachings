# From 2 lists, using a list comprehension, create a list containing:
#
# [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]
#
#      colors = ['Black', 'White']
#      sizes = ['s', 'm', 'l', 'xl']
# If the tuple pair is in the following list, it should not be added to the comprehension generated list.
#
#      soled_out = [('Black', 'm'), ('White', 's')]

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
soled_out = [('Black', 'm'), ('White', 's')]

clothing_list = [(color, size) for color in colors for size in sizes if (color, size) not in soled_out]

print(clothing_list)