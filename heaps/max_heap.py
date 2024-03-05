# we will create a max heap class:



class MaxHeap:
    def __init__(self):
        self.heap = []  # the constructor will only create an empty list that we will later add to

    # next we will create some helper methods that will make the rest of the class easier, the next 
    # 4 methods will be the helper methods:
    def left_child(self,index):  # we will use zero indexing
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def parent(self, index):
        return (index - 1) // 2  # integer division will remove anything to the right of the decimal place after performing the calculation 
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]  # pretty easy to swap positions in a list in python

    def sink_down(self, index):
        max_index = index 
        # next we will  create a while loop that we will break out of with a return statement at the end
        while True:
            # first we point to the left and right child of the popped index:
            left_index = self.left_child(index)
            right_index = self.right_child(index)
            # we will guard against the possibility that the popped index has no children in our if statements:
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index  # max will now point to left index 
            # next we will compare the new max to the right index if there is one:
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            # lastly we will check to see if the max is already where it should be:
            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return  # if we are done we are done 

                
    


    # we should also add a print function to the class:
    def print_max_heap(self):  # i don't think we really need this print method, i will leave it 4 now 
        for i in self.heap:
            print(i) 

    # next we will add an insert method to the mix:
    def insert(self, value):  # O(log n)
        self.heap.append(value)  # start by appending the value to the list, from there we will compare to the parent if there is one
        current = len(self.heap) - 1  # will be 0 if there are no values in the tree other than the one we just added and while loop will never run

        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:  # this will end the loop if the value has reached index 0 or is less than the parent 
            self.swap(current, self.parent(current))  # swap the indices if the loop evaluates to true
            current = self.parent(current)  # move current to point at the parent index, which is now the value we added and do the loop again if needed                                                                      

        return True  

    # we will next create the remove method,
    # with a heap we will only ever remove the item at the top of the heap, whether it is a min or a max heap,
    # we will need a helper method and we will call it sink_down, see above:
    def remove(self):  # # O(log n) 
        # first we code for when we have no items in heap:
        if len(self.heap) == 0:
            return None 
        # next we code for when we have 1 item in the list:
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # if the heap is greater than one in length we will create a max to return later 
        max_value = self.heap[0]  
        # next we will make the last element in the list the new 0th index:
        self.heap[0] = self.heap.pop()  # .pop will remove and return the last element of the list and we made it the 0th index
        # we will next call the helper function sink down with a parameter of 0:
        self.sink_down(0)
        return max_value  


mh = MaxHeap()

print(mh.insert(95))

mh.insert(75)

mh.insert(80)

mh.insert(55)

mh.insert(60)

mh.insert(50)

mh.insert(65)

print()

# mh.print_max_heap()

print(mh.heap)

mh.remove()

print(mh.heap)

mh.remove()

print(mh.heap)