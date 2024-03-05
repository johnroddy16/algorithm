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
    
    def pop(self):  # with .pop we must start at the beginning of the ll and work our way through:
        if self.length < 1:
            return None 
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None 
        return temp.value  # temp will just return the hex id:   





            
        





l_l = LinkedList(4)
l_l.append(6)
l_l.print_list()
l_l.append(8)
l_l.append(14)
l_l.print_list()

cool_j = LinkedList(4)
cool_j.append(8)
cool_j.append(16)
cool_j.append(32)
cool_j.append(64)
cool_j.append(128)
cool_j.print_list()
print(cool_j.pop())
print(cool_j.pop())
print(cool_j.pop())
print(cool_j.pop())
print(cool_j.pop())
print(cool_j.pop())
print(cool_j.pop())
cool_j.print_list()
print(cool_j.length)
print(cool_j.head)
