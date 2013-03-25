from Graph import *
import random
import math
from GraphWorld import *

class RandomGraph(Graph):

    """No need for an initializer here, as a RandomGraph will be constructed in the same
    way as a Graph."""
        
        
    """Exercise 4"""
    """This method takes a probability p as a parameter and, starting with an edgeless 
    graph, adds edges at random so that the probability is p that there is an edge 
    between any two nodes."""
    
    def add_random_edges(self, p):
        
        """Check first to make sure p is between 0 and 1."""
        
        if p < 0 or p > 1:
            raise CustomError('p has to be a probability between 0 and 1.')
            
        """Get the number of vertices in the graph."""
        
        num_vertices = len(self.vertices())
        
        
        """As we cycle through pairs of vertices, """

        for v in self.vertices():
            for w in self.vertices():
                random_number = random.random()
                if random_number < p and v != w:
                    e = Edge(v, w)
                    self.add_edge(e)
                else:
                    pass
                    
"""Exercise 6"""
"""Currently, to create a Random Graph G(n, p) requires that we instantiate using:

    g = RandomGraph(n), 

and then do 

    g.add_random_edges(p).

What we want to do in Exercise 6 is to generate many graphs for values of p for a 
given n, and then iterate the same over many values of n.

Hence, the first step is to write a function that generates m random graphs for
a given value of n, iterating over m values of p for each graph generated."""

def generate_random_graphs(n, m, p):

    #n is the number of nodes
    #m is the number of graphs to generate
    #p is the specified probability
    
    graphs = [] #this is a list of graphs

    while len(graphs) < m:
        labels = string.lowercase + string.uppercase
        vs = [Vertex(c) for c in labels[:n]]
        g = RandomGraph(vs) #Create a graph with n vertices.
        g.add_random_edges(p)

        graphs.append(g)
    
    return graphs
    
"""The following method counts the number of graphs within the list of graphs that are
connected, and returns that number, which can be printed on the screen."""
def count_connectivity(graphs):
    counter = 0
    for graph in graphs:
        if graph.is_connected():
            counter += 1
        else:
            pass
    return counter
        
        
def main(script, *args):
    n = 20 #number of nodes
    m = float(15) #number of graphs
    
    ps = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    
    connectedness = []
    
    for p in ps:
    	graphs = generate_random_graphs(n, m, p)
    	fraction = float(count_connectivity(graphs)/m)
    	connectedness.append((n, p, fraction))
    
    for row in connectedness:
    	print row
    

#     for graph in graphs:
#         layout = CircleLayout(graph)
# 
#         #draw the graph
#         gw = GraphWorld()
#         gw.show_graph(graph, layout)
#         gw.mainloop()


if __name__ == '__main__':
    import sys
    main(*sys.argv)
