# we will now create a min heap class:

class MinHeap:

    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        min_index = index
        
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]):
                min_index = left_index

            if (right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]):
                min_index = right_index

            if min_index != index:
                self._swap(min_index, index)
                index = min_index
            else:
                return 
            
    def insert(self, value):  # O(log n)
        self.heap.append(value)  # start by appending the value to the list, from there we will compare to the parent if there is one
        current = len(self.heap) - 1  # will be 0 if there are no values in the tree other than the one we just added and while loop will never run

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:  # this will end the loop if the value has reached index 0 or is less than the parent 
            self._swap(current, self._parent(current))  # swap the indices if the loop evaluates to true
            current = self._parent(current)  # move current to point at the parent index, which is now the value we added and do the loop again if needed                                                                      

        return True 
    
    def remove(self):
        # first we code for when we have no items in heap:
        if len(self.heap) == 0:
            return None 
        # next we code for when we have 1 item in the list:
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # if the heap is greater than one in length we will create a max to return later 
        min_value = self.heap[0]  
        # next we will make the last element in the list the new 0th index:
        self.heap[0] = self.heap.pop()  # .pop will remove and return the last element of the list and we made it the 0th index
        # we will next call the helper function sink down with a parameter of 0:
        self._sink_down(0)
        return min_value
    


minh = MinHeap()
print(minh.heap)

minh.insert(12)
minh.insert(10)
minh.insert(8)
minh.insert(6)

print(minh.heap)

minh.insert(4)

print(minh.heap)

minh.insert(2)

print(minh.heap)

minh.remove()

print(minh.heap)