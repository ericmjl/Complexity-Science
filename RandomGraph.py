from Graph import *
import random
import math

class RandomGraph(Graph):

	"""No need for an initializer here, as a RandomGraph will be constructed in the same
	way as a Graph."""
		
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
		
	