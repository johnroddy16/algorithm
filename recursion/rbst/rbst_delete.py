# we will create the method for recursive delete and then copy the code over to trees/binary-search-trees.py to test the method:

# recursive delete will need a helper method for times when we want to delete and node that has 2 subtrees, the helper method will be known as min_value:

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

# return current_node.value, will go in the helper method min_value when we create it, notice we do not return the node, just the value of the node 
# the helper method min_value:
    
def min_value(self, current_node):
    while current_node.left:  # could write is not None 
        current_node = current_node.left  # we just traverse to the left searching for smaller values
    return current_node.value  # we return only the value, not the entire node with pointers and all 