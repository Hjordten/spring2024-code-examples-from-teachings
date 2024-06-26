
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Additional basic list exercises

# D. Given a list of numbers, return a tuple where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns (1, 2, 3). You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
        new_list = []
        for item in nums:
             if item not in new_list:
                  new_list.append(item)
        new_list = tuple(new_list)          
        return new_list
    

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    return sorted(list1 + list2)

# linear solution
#def linear_merge(list1, list2):
    #result = []
    #i1 = 0
    #i2 = 0

    # Loop until one of the lists is exhausted
    #while i1 < len(list1) and i2 < len(list2):
        # Compare the current elements of both lists
     #   if list1[i1] <= list2[i2]:
            # Append the smaller element to the result list
      #      result.append(list1[i1])
            # Move to the next element in list1
           # i1 += 1
       # else:
            # Append the smaller element to the result list
        #    result.append(list2[i2])
            # Move to the next element in list2
         #   i2 += 1

    # Append any remaining elements from list1
    #while i1 < len(list1):
     #   result.append(list1[i1])
      #  i1 += 1

    # Append any remaining elements from list2
    #while i2 < len(list2):
     #   result.append(list2[i2])
      #  i2 += 1

    #return result


# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print (f'{prefix} got: {got} expected: {expected}')


# Calls the above functions with interesting inputs.
def main():
    print()
    print('remove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), (1, 2, 3))
    test(remove_adjacent([2, 2, 3, 3, 3]), (2, 3))
    test(remove_adjacent([]), ())

    print()
    print('linear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


main()