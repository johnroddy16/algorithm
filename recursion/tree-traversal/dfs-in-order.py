# there are 3 ways to write depth first search, here we will write the code 4 dfs in order:

# we will as always copy to binary-searcg-tree when complete and ready to run:

# with dfs in order we go left until we cannot anymore, write the value to results, then try to go right, with this technique we will end up with a list of 
# values in ascending order:

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








# dfs pre order is just here as a reference to write dfs in order:    

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
    return results  