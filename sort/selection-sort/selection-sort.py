# selection-sort:

# with selection sort we create a var called min index and store the index with the lowest value, not the value itself: 


nums = [4, 2, 6, 5, 1, 3]
print(nums)
print('nums sorted:')

def selection_sort(l):
    for i in range(len(l) - 1):  # for i in range(5), which is 0 1 2 3 4 
        min_index = i  # first time thru 0, final time thru in the case of our six item list 4 
        # we now need to compare this index to all other indexes in the list that come after it:
        for j in range(i+1, len(l)):  # first time thru 1, 6 in our case, meaning 1-5, 1 2 3 4 5 
            # j will be 1 the first time thru:
            if l[j] < l[min_index]:
                min_index = j  # in our list min_index will become 1 after the first comparison first time thru, then eventually become 4 
            # do a swap if needed after each time thru the loop:
        if i != min_index:    
            temp = l[i]  # first time thru l[0], 4 
            l[i] = l[min_index]  # first time thru l[0] = l[1], l[1] is 2 
            l[min_index] = temp  # first time thru l[1] = 4, which was held in temp  
    return l
    
x = selection_sort(nums)
print(x)  # [1, 2, 3, 4, 5, 6], pretty cool function 