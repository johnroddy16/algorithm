# adding reverse method to linked list class: 
# very important to know how to reverse a linked list 

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
    def append(self, value):  # O(1)
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
    
    def pop(self):  # O(n), with .pop we must start at the beginning of the ll and work our way through:
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
        return temp
    
    def prepend(self, value):  # O(1)
        new_node = Node(value)
        if self.head is None:  # could write if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1 
        return True  # optional
    
    def pop_first(self):  # O(1)
        # pass 
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp 
    
    def get(self, index):  # O(n)
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        for _ in range(index):
            temp = temp.next 
        return temp 
    
    def set_value(self, index, value):  # O(n)
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False 
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next 
        temp.next = new_node
        self.length += 1
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False 
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index-1)
        remove_node = temp.next
        temp.next = remove_node.next
        remove_node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None 
        return remove_node
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp 
        after = temp.next
        before = None 
        for _ in range(self.length):
            after = temp.next # already does in first iteration 
            temp.next = before  # this flips the pointer
            before = temp  # moves before up one
            temp = after  # moves temp up one 
            # and that is that 

# we shall once again test the method:

ll = LinkedList(2)
ll.append(4)
ll.append(6)
ll.append(8)

ll.reverse()

ll.print_list()