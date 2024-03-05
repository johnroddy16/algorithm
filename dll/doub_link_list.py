# our constructor for a doubly linked list:

class Node:
    def __init__(self, value):  
        self.value = value
        self.next = None
        self.prev = None  # the only difference in the node is a pointer to the previous value 


class DoublyLinkedList:  # linked list constructor 
    def __init__(self, value):
        new_node = Node(value)  # will call the Node class and we will pass value to it
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):  # O(n)
        temp = self.head  # this creates a temporary variable that will point to the head
        while temp is not None:
            print(temp.value)  # will print the value of temp if not None
            temp = temp.next

    def append(self, value):  # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node 
        self.length += 1 
        return True 

        # with append we need to have the pointer of the last node point to
        # the new node and we need to have tail also point to the new node
        # the new node will point to None as next and we need to have it point to self.tail as prev:

    def pop(self):  # O(1)
        if self.length < 1:  # could say if self.length == 0:    
            return None 
        temp = self.tail 
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            temp = self.tail 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1 
        return temp

    def prepend(self, value):  # O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
        self.length += 1
        return True  # optional 
    
    # def pop_first(self):  # O(1)  # this is my original code and below it is refactored to be a little cleaner 
    #     if self.length == 0:
    #         return None
    #     temp= self.head
    #     if self.head.next is not None:
    #         self.head.next.prev = None
    #     self.head = self.head.next
    #     temp.next = None
    #     self.length -= 1
    #     if self.length == 0:
    #         self.tail = None 
    #     return temp
    
    def pop_first(self):  # O(1)
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp 
    
    # def get(self, index):  # O(n) finally O of n in a dll
    #     if index < 0 or index >= self.length:
    #         return None 
    #     temp = self.head
    #     for _ in range(index):
    #         temp = temp.next
    #     return temp  # this all works fine just like in a linked list but there is a way to optimize this in a dll:
    
    def get(self, index):  # we will now optimize the get method
        # we can start at the tail of the dll if it makes sense to do so 
        # for that we have to change some code:
        if index < 0 or index >= self.length:
            return None 
        temp = self.head
        # here come the changes:
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next  # i.e. if the index is in the first half of the list start from the head and find the index
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp 
    
            # x = index - self.length  # i love what i wrote here and it totally works but what is in it's place is cleaner 
            # y = (x * (-1)) - 1
            # for _ in range(y):
            #     temp = temp.prev

    # def set_value(self, index, value):  # this was fun to write but below is way better using the get method
    #     if index < 0 or index >= self.length:
    #         return None
    #     temp = self.head
    #     if index < self.length / 2:
    #         for _ in range(index):
    #             temp = temp.next
    #     else:
    #         temp = self.tail
    #         for _ in range(self.length - 1, index, -1):
    #             temp = temp.prev 
    #     temp.value = value 
    #     return temp
    
    def set_value(self, index, value):
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
        before = self.get(index - 1)  # the next few lines are better that the below code 
        after = before.next
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node 
        self.length += 1
        return True
        # temp = self.get(index)  # this works and is cool but there is a better way that replaced it in insert method 
        # new_node.prev = temp.prev
        # temp.prev.next = new_node
        # temp.prev = new_node
        # new_node.next = temp

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop() 
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None 
        self.length -= 1
        return temp  
    
    # instead of using before and after we can just use temp and write:
    # temp = self.get(index)
    # temp.next.prev = temp.prev
    # temp.prev.next = temp.next




 




      
 

        

    
    
     
        
    

        

          

    



# our first test 11-17-23:

dll = DoublyLinkedList(4)

dll.append(8)

dll.pop()

dll.pop()

dll.append(4)

dll.append(8)

dll.pop()

dll.pop()

dll.pop() 

dll.prepend(4)

dll.prepend(2)

dll.append(6)

dll.append(8)

dll.prepend(0)

dll.prepend(-2)

dll.append(10)

dll.pop_first()

# dll.insert(0, 24)

# dll.pop_first()

# dll.pop_first()

# dll.pop_first()

# dll.pop_first()

# dll.pop_first()

# dll.pop_first()

# dll.pop_first()

# print(dll.get(0).value)

# print(dll.set_value(6, 16)) 

# dll.insert(2, 24)

print(dll.remove(4).value)

print() 

dll.print_list()
print('list length:', dll.length) 
# print('list head:', dll.head)
# print('list tail:', dll.tail)
# print('list head previous:', dll.head.prev)
# print('list head next:', dll.head.next)
# print('list tail previous:', dll.tail.prev)
# print('list tail next:', dll.tail.next) 