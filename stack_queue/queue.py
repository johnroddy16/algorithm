# we will now create a queue class
# i will attempt on my own with a ll and then watch the lectures after to compare code:

# first we create the contructor for the Node and Queue, then we will create a print_queue method:

class Node:
    def __init__(self, value):  
        self.value = value
        self.next = None  # we will use a ll and enqueue from what would normally be the tail since it is O(1) and dequeue from what would normally be the head since that is also O(1)

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first 
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):  # enqueue will be like append with a ll O(1)
        new_node = Node(value)
        if self.length == 0:  # could write if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True  # optional in this case 
        
        
    
    def dequeue(self):  # dequeue will be like prepend with a ll O(1)
        if self.length == 0:
            return None
        temp = self.first
        self.first = temp.next  # could write self.first = self.first.next 
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.last = None  # we could write an if statement that will run if the queue length is 1 instead of this if statement at the end 
        return temp           # that code would be: if self.length == 1: self.first = None, self.last = None, then we would add an else statement with the rest of the code 





q = Queue(4)

q.enqueue(3)

q.enqueue(2)

print(q.dequeue().value)

print(q.dequeue().value)

print(q.dequeue().value)

print(q.dequeue())

print()

print('length:', q.length)

print('first:', q.first)

print('last:', q.last)

q.print_queue()