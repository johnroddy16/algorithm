# the bulit-in hash table in python is the dictionary

# a collision is when we attempt to store a key-value pair at an address that already contains a key-value pair
# if we decide to store it there we call the technique separate chaining
# if we decide to continue on and look for an empty address we call it linear probing and it is a form of open addressing 
# the technique of linear probing ensures that we do not have more than one key-value pair stored at any one address 

# when using separate chaining we can store all key-value pairs as lists in a list of lists or in a linked list where we iterate thru the linked list at that 
# address when looking for an item  

# using a prime number of addresses increases the randomness of where items will be stored and decreases the chances of a collision 