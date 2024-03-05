# there are 3 ways in which to implement depth first search and we will look at all 3:

# first we will look at is called preorder:

# this will involve creating a recursive function within the method:

# when complete we will add to binary-search-tree and test the method on our tree:

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