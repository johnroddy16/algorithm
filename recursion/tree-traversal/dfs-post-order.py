# there are 3 ways to write dfs, this will be the file 4 post order:

# we will copy to binary-search-tree when it is complete:

# with post order we will go to the left until we cannot anymore and check to the right once we can no longer go left, if nothing to the right we then write the value of the node
# to results list, pretty simple: 

# let us write the code: 


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
    
# next we will write the code 4 dfs in order 