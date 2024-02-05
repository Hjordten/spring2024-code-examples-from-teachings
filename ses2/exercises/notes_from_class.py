original_list = ['Hello', 'World', 'Huston', 'we', 'are', 'here']

world_houston_we_are = original_list[1:5]
print (world_houston_we_are)

hello_world = original_list[0:2]
print(hello_world)

are_here = original_list[4:]
print (are_here)

are = original_list[4:5]
print(are)

#hello_houston_are = [original_list[0], original_list[2], original_list[4]]
hello_houston_are = original_list[::2]
print(hello_houston_are)

here_are_we_houston_world_hello = original_list[::-1]
print(here_are_we_houston_world_hello)

# SET

names ={'Hans', 'Peter', 'Henning'}
members ={'Hans', 'Peter'}

# convert set to list
list(names)


# convert list to set
new_set = set(names)

print (new_set)
