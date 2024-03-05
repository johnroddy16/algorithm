# to append to a linked list we will have the last item in the list point to the new node
# and tail point to the new node
# this is O(1) since it is the same amount of operations not matter how long the ll:

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

    def print_list(self):
        temp = self.head  # this creates a temporary variable that will point to the head
        while temp is not None:
            print(temp.value)  # , end='', will print the value of temp if not None
            temp = temp.next 
        # print()
    def append(self, value):
        # with append we need to have the pointer of the last node point to
        # the new node and we need to have tail also point to the new node
        # the new node will point to None as constructed:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True  # not necessary to return True here, optional
    


# let us test the code today:

newll = LinkedList(8)

print(newll)  # <__main__.LinkedList object at 0x7f9fbf680b80>

newll.print_list()  # 8

newll.append(16)


newll.print_list()  # 8 16

newll.append(32)
newll.append(64)
newll.print_list()  # 8 16 32 64

print()

x = newll.head.value
print(x)
y = newll.tail  # <__main__.Node object at 0x7ff2ca7659a0>
z = newll.tail.value
print(y)
print(z)  # 64 
print(newll.head.next.value)  # 16
print(newll.head.next.next.value)  # 32 