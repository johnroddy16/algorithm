# we will now create a graph class and start by adding the add_vertex method:

class Graph:
    def __init__(self):
        self.adj_list = {}  # we create an empty dict to start with the contructor 

    # let us make a method to print the graph:
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])  # we will output the vertex and the edges, if any are there 

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():  # here we check to see if we already have the vertex 
            self.adj_list[vertex] = []  # we make the new vertex a key for the dict and set the value to an empty list, we have not added edges yet
            return True
        return False 
    
    # next we will create an add edge method to our graph class:
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False 

    # we will tackle the remove edge method next:
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # we must create a try and except block to account for values that do not share or have an edge:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass  
            return True 
        return False 
    
    def remove_vertex(self, vertex):
        # in order to remove a vertex we must first remove all edges from it, i will first try on my own:
        if vertex in self.adj_list.keys():
            for i in self.adj_list[vertex]:
                self.adj_list[i].remove(vertex)
            del self.adj_list[vertex]
            return True 
        return False  # this is a beautiful function and i had to watch the video to make it this clean, my code worked but it was not efficient 
        





g = Graph()

g.add_vertex('A')  # so far we have A : [] if we print it out, one vertex A with no edges

g.add_vertex('B')  # we will create another vertex so we can test the add_edge method 

g.add_vertex('C')

g.add_vertex('D')

g.add_vertex('E')

print(g.add_edge('A', 'B'))  # True or False depending on the evaluation of the add_edge method 

g.add_edge('A', 'C')

g.add_edge('B', 'C')

g.add_edge('D', 'A')

g.add_edge('D', 'B')

g.add_edge('D', 'C')

# g.remove_edge('A', 'B')

# g.remove_edge('A', 'D')  # initially ran when A and D did not share an edge, ran fine due to the try and except block in the method 

print(g.remove_vertex('D')) 

print()

g.print_graph()