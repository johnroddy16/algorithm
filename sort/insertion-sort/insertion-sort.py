# insertion-sort:

# with insertion sort we always start with the second item in the list and we compare it to the item before it and then we go to the next index and start comparing
# backwards, the item that ends up in the 0 spot in a list will be special case and we will code 4 that:

# we will start with a list that only has 2 items out of order:

nums = [1, 2, 4, 3, 5, 6]

nums_1 = [4, 3, 5, 1, 6, 2]

def insertion_sort(my_list):
    for i in range(1, len(my_list)):  # we include the 1 here so we can start at index 1 instead of 0, remember we compare back
        temp = my_list[i]  # first time thru with nums temp = 2
        j = i - 1  # this will give us j = 0 first time thru nums 
        while temp < my_list[j] and j > -1:  # first time thru 2 < 1, False and while loop will not run, but will when we get to my_list[j] = 4 
            my_list[j + 1] = my_list[j]  # [j + 1] is where temp was and [j] is the greater value being swapped for the lesser 
            my_list[j] = temp  # replace my_list[j] with temp, the lesser value 
            j -= 1  # push j back 1 
    return my_list

# and j > -1: is there for the edge case where the value is pushed all the way to index 0 and there is no value to the left of it to compare it to 

x = insertion_sort(nums)

print(x)  # [1, 2, 3, 4, 5, 6] seems to work 

y = insertion_sort(nums_1)

print(y)  # [1, 2, 3, 4, 5, 6] 