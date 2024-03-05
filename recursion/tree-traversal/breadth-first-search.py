# breadth first search:

# width breadth first search we create 2 empty lists, one called queue and one called results, we will return results
# we start by adding the root to queue, then move it to results, we then check to see if there is a left node and right node, if so
# we add them to queue, then move the left node to results and check to see if there is a left and right node, if so add to queue, move
# next in queue to results, check for left and right nodes, if there add to queue, and so on........
# the loop we write for this will only run as long as there is an item in the queue
# that would mean that we visited every item in the tree and now we just need to return results:

# the code, to be added to binary-search-tree.py:

# breadth first search:

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
    return results  # pretty simple, i do not expect depth first to be so easy, we shall see, depth first was easy and i was wrong 