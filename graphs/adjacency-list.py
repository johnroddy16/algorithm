# adjancency list:

# see black note book 11-26-23 graphs for a look at the graph that we are using for the example adjacency list:

# we will use a dict to make the adj list:

adj_list = {  # in this dict the key will be the vertex and the value(s) will be the vertex or vertices that key vertex has an edge with
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['A', 'D'],
    }  

print(adj_list)