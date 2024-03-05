# a common interview question for hash tables:

# we will have 2 lists and need to determine if the 2 lists have a common element:

# first and slow way with nested loops O(n**2):

def matched(l1, l2):  # O(n**2)
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False 

# the better and faster way:

# using a python dictionary we can add the values of the first list to the dict and then see if any items from the second list match:

x = [1, 2, 5]

y = [0, 4, 6]


def matching(l1, l2):  # O(2n) = O(n), better  
    nums = {}
    for i in l1:
        nums[i] = True
    for i in l2:
        if i in nums:
            return True
    return False 

print(matching(x, y))