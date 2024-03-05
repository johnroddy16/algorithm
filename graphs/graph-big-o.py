# big O 4 graphs:

# big O for space complexity:

# when using a matrix we have to store all of the 0s where there are no edges shared along with the 1s or weights we store:
# O(|V|^2)  vertices squared

# when using a adj list we only need to store the vertex and those vertices with which it shares an edge:
# O(|V|+|E|)  vertex + edges, less space taken 

# when adding a vertex to a matrix we get O(|V|^2), we basically have to rewrite the entire matrix
# when adding a vertex to an adj list we get O(1), faster 

# when adding an edge both adj matrix and adj list are O(1)

# when removing an edge with adj matrix we get O(1), we just change the 1s to 0s
# when removing an edge with adj list we have O(|E|), O of the number of edges, since we may have to iterate thru a list of edges to remove the edge, a win 4 the matrix this time 

# when removing a vertex with a matrix we get O(|V|^2), we basically have to rewrite the entire matrix again
# when removing a vertex with a list we get O(|V|+|E|), we will need to go thru everything in the list and remove any edges that match the removed vertex, a win 4 the list again 



# overall adj lists are better than adj matrix 