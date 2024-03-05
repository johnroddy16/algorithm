# in a binary search tree if a node's value is greater than the parent node's value than the new node is placed to the right of the parent, 
# opposite for a node with a value less than the parent node and we always start by comparing the new_node to the root node and working down from there:

# we treat binary search trees like O(log n) since we are going to assume it does not just become a ll or something close to that

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.root = new_node  # we can write it this way and we can also write it another way, see below
    def __init__(self):
        self.root = None  # here we have a complete contructor 4 a binary search tree that creates an empty tree, we can insert nodes later 

    # insert:

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True 
        temp = self.root
        while True:  # we will break the loop when we hit a return statement at some point in the future 
            if new_node.value == temp.value:  # we need .value since we are comparing the values 
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True  # get out of the loop 
                temp = temp.left  # this will occur so we can make our next comparison if the nested if statement evaluates to false 
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right 
         
    # contains will simply check to see if a tree contains a certain value:

    def contains(self, value):
        if self.root == None:
            return False 
        temp = self.root
        while True:  # we will end the loop with a return of some kind 
            if temp.value == value:
                return True 
            if value < temp.value:
                if temp.left is None:
                    return False 
                temp = temp.left
            if value > temp.value:
                if temp.right is None:
                    return False 
                temp = temp.right  # i wrote this one on my own with no pencil and paper and no video 

    # there is another really nice clean way to write the contains method:

    def contaiins(self,value):  # wrote this one spelled contaiins so i can try both methods 
        # if self.root == None:
        #     return False  # we do not need these first two lines, if the root is None the loop will not run and False will be returned 
        temp = self.root  # if root is None the loop will never run and False will be returned 
        while temp:  # is not None
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True  # we return True here, the value has been found in this case 
        return False  # if the loop ends without returning True before temp is None 
            

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)  
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def min_value(self,current_node):
        while current_node.left:  # could write is not None 
            current_node = current_node.left  # we just traverse to the left searching for smaller values
        return current_node.value  # we return only the value, not the entire node with pointers and all 
    
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None  # the base case 
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        # most of the code for this method will be in the else statement where we code for when we have found the node to delete
        # we have to code for when the node is a leaf, has a left subtree, has a right subtree or has both a left and right subtree
        # this is where the helper method min_value comes into action:
        else:  
            if current_node.left == None and current_node.right == None:
                return None  # leaf node 
            elif current_node.left == None:
                current_node = current_node.right  # right subtree, the deleted node will be garbage collected as now nothing points to it 
            elif current_node.right == None:
                current_node = current_node.left  # left subtree 
            else:  # this is where the helper method min_value comes in:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min  # current node.value is the value from the node to delete, we only copy the value here, not the entire node 
            # now we must delete the node at sub_tree_min:
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)  # subtree left and right 

        return current_node 
        # when we have subtrees at left and right we need to find the min value of the right subtree and copy it to the space left by the deleted node
    
    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)

    def BFS(self):  
        current_node = self.root 
        queue = []  # as we learned in queues lectures a list is not the best way to create a queue, we use it here for simplicity
        # here we just want to focus on the mechanics of creating the bfs 
        results = []
        queue.append(current_node)  # this is the entire node, not just the value, it includes left and right of current_node 
        # important to add initial current_node to queue before starting while loop since while loop will run until queue empty:
        while len(queue) > 0:
            current_node = queue.pop(0)  # will set current_node equal to 0th item in queue and pop item from queue
            results.append(current_node.value)  # not the entire node, just the value, we need the node 
            if current_node.left:  # could write if current_node.left is not None:
                queue.append(current_node.left)  # the entire node
            # do the same thing to the right of the node:
            if current_node.right:  # could write if current_node.right is not None:
                queue.append(current_node.right)
        # only thing left to do is return the results list:
        return results
    
    def dfs_pre_order(self):
        results = []
        # next we define a recursive function to add values to results, keep the call stack in mind:
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results  # pretty simple actually, just have to remember the call stack and what it does to assist in recursion
    
    def dfs_post_order(self):
        results = []  # to be returned at the end 
        # the recursive function will be very similar to pre order:
        def traverse(current_node):
        
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right) 
            results.append(current_node.value)  # this is the first line of the function in pre order, here it sits in post order 

        traverse(self.root)  # run it on the root to get things started 
        return results  # and that is that, always remember what the call stack does to play a role in the order of things within a recursive function
    
    def dfs_in_order(self):
        results = list()
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results






t = BinarySearchTree()

t.r_insert(47)

t.r_insert(21)

t.r_insert(76)

t.r_insert(18)

t.r_insert(27)

t.r_insert(52)

t.r_insert(82)

# t.insert(47)

# t.insert(21)

# print(t.insert(76))

# print(t.insert(18))

# t.insert(27)

# t.insert(52)

# t.insert(82)

# t.insert(-5)

# print()

# print(t.contaiins(-16))

print()

print(t.r_contains(4))  # False

print(t.r_contains(26))  # True 

# print('root:', t.root.value, 'left:', t.root.left.value, 'right:', t.root.right.value)  # intially None 

# print('bst contains 27:', t.r_contains(27))
# print('bst contains 16:', t.r_contains(16))

print('root:', t.root.value)
print('left:', t.root.left.value)
print('right:', t.root.right.value)
# t.delete_node(82)
try:
    print(t.root.right.right.value)  # 82, this works, added the try except black to make sure 82 is deleted  
except:
    print('value is None so no value')
# t.delete_node(18)

print(t.min_value(t.root))  # we can run min_value on the root or on a subtree, when we delete 18 this changes from 18 to 21, looks good 
print(t.min_value(t.root.right))  # here is the helper method min_value run on a subtree  

x = t.BFS() 
print(x)  # [47, 21, 76, 18, 27, 52, 82] looks like BFS works with these values, the list created is in the same order in which we created the tree, cool 

y = t.dfs_pre_order()
print(y)  # [47, 21, 18, 27, 76, 52, 82], different order than BFS() 

z = t.dfs_post_order()
print(z)  # [18, 27, 21, 52, 82, 76, 47], different order than pre order 

a = t.dfs_in_order()
print(a)  # [18, 21, 27, 47, 52, 76, 82], i think i wrote it perfectly, this one i did without the video 