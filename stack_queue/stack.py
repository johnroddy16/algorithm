# we will implement the stack using a linked list where we will push and pop from the 
# top (head) of the ll since pushing and popping from there will be O(1)
# we could use a normal list but we are trying to learn something here:

# we will first create the contructor for the node, very similar to ll and dll:

class Node:
    def __init__(self, value):  
        self.value = value
        self.next = None  # no self.prev as this is a ll and not a dll

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node  # like self.head
        # we could add self.bottom here but we will only be dealing with one end so no need
        self.height = 1  # add height instead of length       

    def print_stack(self):
        temp = self.top  # only difference 
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node 
        else: 
            new_node.next = self.top
            self.top = new_node
        self.height += 1 

    def pop(self):
        if self.height == 0:
            return None 
        temp = self.top 
        self.top = temp.next  # could write self.top = self.top.next 
        temp.next = None 
        self.height -= 1
        return temp 

    
    




s = Stack(8)

s.push(2)

s.push(1)

print(s.pop().value)

print(s.pop().value)

s.pop()

s.pop()

print()

print('height:', s.height)

print('top:', s.top)

s.print_stack()