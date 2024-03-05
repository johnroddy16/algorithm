# big O of lists:

nums = [11, 3, 23, 7]

nums.append(17)

nums.pop()    # with no argument will take off the last item of the list

print(nums)

# .append and .pop (with no argument) are O(1) since it is always one operation


# if we play with the first element of a list then we write O(n) since we have to reindex everything when we 
# add or take away from the start of a list:
# this will be significant when we use .pop(0) and .insert(0, 16) (16 could be any number):

nums.pop(0)    # not as fast as popping from end of list

nums.insert(0, 11)    # not as fast as .append

print(nums)    # back to the list we started with

# what if we index to the middle of the list somewhere?:

nums.insert(1, 'hi')    # also O(n) since we must reindex all after index 1 now
print(nums)

# remember that big O always measures worst case

# in nums if we search for a number with the value of the number we write O(n) since we have to search the entire list worst case
# to find the number
# if we search by index we can go stright to the place in memory and find the value and write O(1)