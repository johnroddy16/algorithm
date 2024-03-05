# creating a node class:

# what is a node in a linked list? It is really this:

# the node is the value and the pointer. it is essentially a dictionary

node = {
    'value': 4,
    'next': None 
}

# a value and direction to the next node, in this case it is the tail node as it does not point to another node

class Node:
    def __init__(self, value):  # this basically creates what is seen on line 7
        self.value = value
        self.next = None

class LinkedList:  # linked list constructor 
    def __init__(self, value):
        new_node = Node(value)  # will call the Node class and we will pass value to it
        self.head = new_node
        self.tail = new_node
        self.length = 1

ll = LinkedList(4)  # we have created the head and tail of the linked list ll
print(ll.head.value)  # 4
print(ll.head.next)  # None
print(ll.length)  # 1
print(ll.tail.value)  # None 