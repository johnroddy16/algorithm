# merge sort:

# idea behind merge sort:

# it is easy to merge and sort 2 lists that are already sorted
# if we start with a list containing 8 numbers [1, 5, 4, 3, 8, 7, 6, 2] in merge sort we break the list in half repeatedly until we end 
# up with lists that all contain 1 item and are therefor by definition sorted
# from there we simply combine and sort starting with the 1 item lists then the 2 item lists then the 4 item lists until we have our original list
# of 8 numbers sorted [1, 2, 3, 4, 5, 6, 7, 8]:


# helper function merge:

# what merge does is take 2 sorted lists and combines them into 1 sorted list:

# it does this by iterating thru both lists and comparing values and adding lowest value to new list:

# the code:

def merge(list1, list2):  # we pass merge 2 lists and these lists need to be sorted
    # we will combine the 2 lists into 1 list
    combined = []
    i = 0  # i will point to the first list
    j = 0  # j will point to the 2nd list 
    # we need to use a while loop:
    while i < len(list1) and j < len(list2):  # while both lists still have items in them 
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1 
    # in case we have left overs in list1:
    while i < len(list1):  # if there is anything left in list1 append the item to the list 
        combined.append(list1[i])
        i += 1 
    # in case we have anything left in list2, in our example we will not:
    while j < len(list2):  # if there is anything left in list2 append the item to the list, do not forget to increment j, or i in the previous while loop 
        combined.append(list2[j])
        j += 1 
    # and as always return the list we created:
    return combined 



nums = [1, 3, 7, 8]  # the algorithm will work even if lists share a number 
nums_1 = [2, 4, 5, 6]

x = merge(nums, nums_1)
print(x)  # [1, 2, 3, 4, 5, 6, 7, 8] 

# with merge sort we need to break the list in half over and over until we get 1 item lists then we can use merge to combine into sorted lists:

# we will use recursion to write the code that breaks lists in half:

# remember with recursion we have to be doing the same thing over and over and we have to be making the problem smaller each iteration 
# breaking things in half is making them smaller so we are good there 
# we also must have a base case to perform recursion, in merge sort it will be when len(the list) is 1 

# then we use merge helper function to combine the lists until we have a sorted original list:

# merge sort is different than other sorting algorithms we have seen so far because the others sort the list in place, meaning that the original list will be
# sorted, like with .sort(), but with merge sort the original list remains the same and the algorithm returns a new sorted list, like with sorted()

# the code:

def merge_sort(my_list):
    # base case:
    if len(my_list) == 1:
        return my_list 
    mid_index = len(my_list) // 2 # we use int division to get an integer from a list of uneven length, could write int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])  # this will say my_list[:2] if we have a list of 4 items and will give us [0, 1] indices, basic list slicing 
    right = merge_sort(my_list[mid_index:])  # this will say my_list[2:] if we have a 4 item list and will give us index 2 to the end of list, so [2, 3] indices in a 4 item list 
    # we would like to now call the helper function merge but the sublists need to be sorted first so not quite ready, we may need to split again:
    return merge(left, right)




nums_2 = [3, 1, 4, 2]

midd_index = len(nums_2) // 2
print(midd_index)  # 2 

nums_3 = [1, 3, 2]
midd_index = len(nums_3) // 2 
print(midd_index)

nums_4 = [4, 6, 3, 8, 7, 2, 1, 5]
z = merge_sort(nums_4)
print(z)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(nums_4)  # [4, 6, 3, 8, 7, 2, 1, 5] 

x = merge_sort(nums_3)
print(x)  # [1, 2, 3]

y = merge_sort(nums_2)
print(y)  # [1, 2, 3, 4]  