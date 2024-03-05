# this is supposed to be pretty simple:

def print_list(self):
    temp = self.head  # this creates a temporary variable that will point to the head
    while temp is not None:
        print(temp.value)  # will print the value of temp if not None
        temp = temp.next  # temp will become the next item in the list or None

import nod  # works fine 

from nod import ll  # works fine 


print()

print_list(ll)  # works fine, prints 4, as it should 
    