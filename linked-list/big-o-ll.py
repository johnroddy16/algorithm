# O(1): when we add a node to the end of a ll we have O(1) no matter how long the ll
# all we do is set the last node to point at the new node and set tail to point to
# the new node and set the new node to point to None

# O(n): when we remove an item from the end of a ll we have O(1), we have to make 
# the tail equal to the pointer that points to the new last node and that
# requires running the tail pointer thru the entire list until we reach our goal

# O(1): when we add an item to the front of a ll we have O(1), all we need to do is 
# set the new node to point to the first node and move the head one back to 
# point at the new node, same amount of operations no matter the length of ll

# O(1): when we remove an item from the front of a ll we have O(1) again, all we 
# do is set head to point at the next node and remove the other node from the 
# front, same amount of operations no matter the length of the ll

# O(n): when we need to add a node to somewhere in the middle a ll we have
# O(n) (remember big Omicron is worst case, not best case like Omega or average case
# like Theta), we have to iterate thru the list in order to accomplish this task, set the new node
# equal to the correct pointer then have that poniter point to the new node

# O(n): when we need to remove an item from somewhere in the middle of a ll we have 
# again O(n), we must iterate thru the entire ll to accomplish this, example if we
# want to remove a 4 from in between a 2 and a 6 we need to set the pointer from the 2 
# equal to the pointer from the 4 so that the 2 will then point to the 6, then we can 
# remove the 4 by having it point to none, no memory mangement needed with python, once
# nothing points to the 4 it will be gone via garbage collection 

# O(n): when we want to do a lookup in a ll we have O(n), a ll is not indexed so we
# must iterate thru the list to find the node and worst case it will go thru the 
# entire ll to find the node and big O (Omicron) is worst case, if we lookup by index 
# we also have O(n) as we have to iterate thru the ll

