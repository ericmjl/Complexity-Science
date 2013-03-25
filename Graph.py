""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

class Vertex(object):
	"""A Vertex is a node in a graph."""

	def __init__(self, label=''):
		self.label = label

	def __repr__(self):
		"""Returns a string representation of this object that can
		be evaluated as a Python expression."""
		return 'Vertex(%s)' % repr(self.label)

	__str__ = __repr__
	"""The str and repr forms of this object are the same."""


class Edge(tuple):
	"""An Edge is a list of two vertices."""

	def __new__(cls, *vs):
		"""The Edge constructor takes two vertices."""
		if len(vs) != 2:
			raise ValueError, 'Edges must connect exactly two vertices.'
		return tuple.__new__(cls, vs)

	def __repr__(self):
		"""Return a string representation of this object that can
		be evaluated as a Python expression."""
		return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

	__str__ = __repr__
	"""The str and repr forms of this object are the same."""
	
	def get_length_of_edge(self):
		return len(self)
		
	def get_vertice(self, int):
		return self[int - 1]
	
	def get_vertices(self):
		vertices = []
		x = 0
		while x < len(self):
			vertices.append(self[x])
			x += 1	
		
		return vertices

class Graph(dict):
	"""A Graph is a dictionary of dictionaries.  The outer
	dictionary maps from a vertex to an inner dictionary.
	The inner dictionary maps from other vertices to edges.
	
	For vertices a and b, graph[a][b] maps
	to the edge that connects a->b, if it exists."""

	def __init__(self, vs=[], es=[]):
		"""Creates a new graph.  
		vs: list of vertices;
		es: list of edges.
		"""
		for v in vs:
			self.add_vertex(v)
			
		for e in es:
			self.add_edge(e)

	def add_vertex(self, v):
		"""Add a vertex to the graph."""
		self[v] = {}

	def add_edge(self, e):
		"""Adds and edge to the graph by adding an entry in both directions.

		If there is already an edge connecting these Vertices, the
		new edge replaces it.
		"""
		v, w = e
		self[v][w] = e
		self[w][v] = e

	"""Exercise 2-3"""
	def get_edge(self, v1, v2):
		"""Takes input of two vertices, and returns edge that connects them"""
		"""This code takes advantage of the fact that a KeyError is returned if
		graph[v][w]"""
		
		"""This also takes advantage of the fact that graph[v][w] maps to an Edge if
		there is one, and raises an KeyError otherwise."""
		try:
			if(bool(self[v1][v2])):
				return self[v1][v2]
		except KeyError:
			pass
	
	"""Exercise 2-4"""
	def remove_edge(self, e):
		"""Takes input of an edge, and deletes it from reference."""
		
		"""What this implementation does is to simply take the vertices of the edge
		to be removed, and re-add them to the graph, thereby overwriting the old
		vertices, in the process removing the edge from the graph."""

		try:
			"""will return a list of vertices of the form [v, w]"""
			vertices = e.get_vertices()
			
			for x in vertices:
				self.add_vertex(x)
				
		except ValueError:
			print "The edge cannot be removed."

	"""Exercise 2-5"""
	def vertices(self):
		vertices = []
		for x in self:
			vertices.append(x)
		return vertices
	
	"""Exercise 2-6"""
	def edges(self):
		"""First off, get a list of all the vertices in the graph. Two identical lists
		are used. We will iterate through the first list, calling on get_edge with the 
		paired vertex on the second list.
		
		get_edge will return the edge if it exists, and we will add it to a list called
		'edges'."""
		vertices1 = self.vertices()
		vertices2 = self.vertices()
		
		edges = []
		
		for v1 in vertices1:
			for v2 in vertices2:
				edge = self.get_edge(v1, v2)
				
				if edge == None:
					pass
				else:
					edges.append(edge)
		
		return edges
		
	"""Exercise 2-7"""
	def out_vertices(self, vertex):
		"""Vertices are represented as an object, but in the graph, they are represented
		as a dictionary format, where 
			{Vertex 1: Vertex 2: {Edge e, Vertex 1}, 
					   Vertex 3: {Edge f, Vertex 1}}
		
		To get every vertex associated with vertex v, we will use the list of edges, and 
		use that list to find the edges that contain vertex v. Then, we will append a 
		list containing the other vertices associated with those edges."""
		
		edges = self.edges()
		
		vertices = []
		
		
		for edge in edges:
			if vertex in edge:
				for v in edge:
					if v == vertex or v in vertices:
						pass
					if v != vertex and v not in vertices:
						vertices.append(v)
			if vertex not in edge:
				pass
		
		
		return vertices
	
	"""Exercise 2-8"""
	def out_edges(self, vertex):
		"""Since we have the 'out_vertices' method as specified above, we can use the 
		out_vertices method to get the list of vertices associated with the input vertex
		v, and then use 'get_edge' to get the edge between vertex v and the other 
		vertices."""
		
		"""These are the vertices that are connected to the given vertex. It is a list of
		vertices."""
		out_vertices = self.out_vertices(vertex)
		
		"""Here, we declare a list called 'edges', which is a list of edges connected
		with the vertex."""
		
		edges = []
		
		"""Then, we go through a single loop asking for the edge associated with the given
		vertex and the vertices in out_vertices."""
		
		for v in out_vertices:
			edge = self.get_edge(vertex, v)
			edges.append(edge)
			
		return edges
	
	"""Exercise 2-9"""
	def add_all_edges(self):
	
		"""We have the 'vertices' method that gives us a list of all vertices in the
		graph. Create two lists of vertices that exist within the graph."""
		
		vertices1 = self.vertices() #this is a list
		vertices2 = self.vertices() #this is a list
		
		"""We can create an edge by connecting each vertex with every other vertex."""
		
		"""We also have the 'add_edge' method that allows us to add in an edge, given a
		pair of vertices."""
		
		for v in vertices1:
			for w in vertices2:
				if v != w:
					e = Edge(v, w)
					self.add_edge(e)
					
				if v == w:
					pass
					
		return self
	
	
	"""This method gets all the degrees of the vertices in the graph, and returns a list
	vertex degrees."""
	def get_vertices_degrees(self):
		
		vertices = self.vertices()
		vert_degrees = []
		
		for v in vertices:
			v_deg = len(self.out_edges(v))
			vert_degrees.append(v_deg)
		
		return vert_degrees
			
	
	"""Exercise 3"""
	def add_regular_edges(self, degree):
		
		"""The degree of a vertex is the number of edges it is connected to. For a given 
		graph of n vertices, each vertex v can only be connected to n-1 vertices.
		Therefore, the degree of the vertex can only be less than or equal to the number
		of vertices in the graph minus 1."""
		
		"""Additionally, for a graph of n vertices and a desired degree m, the following
		condition must be fulfilled:
			(m * n)/2 = whole number"""
			
		"""Finally, when populating the graph with edges, priority should be given to
		vertices that do not already have an edge."""
		
		if self.is_valid_degree(degree):
			"""Get the degree of each vertex."""
			degrees = self.get_vertices_degrees()
			
			"""Loop within the list of vertices. Go one vertex pair at a time. The 
			conditions that must be fulfilled to connect two vertices are as follows:
				- v and w cannot be the same.
				- number of edges out of v < degree specified
				- number of edges out of w < degree specified
			The recursion goes as such:
				- start at vertex v.
				- check to see if degree(v) < degree
					- while true: connect edges until degree(v) == specified degree"""
			
			vertices = self.vertices()
			
			for v in vertices:
				while len(self.out_edges(v)) < degree:
					for w in vertices:
						if len(self.out_edges(v)) < degree:
							if len(self.out_edges(w)) == min(degrees) and len(self.out_edges(w)) < degree:
								e = Edge(v,w)
								self.add_edge(e)
								degrees = self.get_vertices_degrees()
								print degrees
								
							if len(self.out_edges(w)) == degree:
								pass		
		
		elif (degree * num_vertices) % 2 != 0:
			raise CustomError('The degree specified cannot be generated for the current graph.')			
					
		elif degree >= num_vertices:
	   		raise CustomError('The degree specified is greater than or equal to the number of vertices.')

		return self
		
	"""This function returns a boolean telling us whether the specified degree is valid
	or not The condition for validity is:
		- degree < number of vertices
		- degree * number of vertices / 2 == whole number."""
		
	def is_valid_degree(self, degree):
	
		"""First, get the number of vertices in the graph."""
		vertices = self.vertices()
		num_vertices = len(vertices)
		
		"""Check to see if:
			- degree is < num_vertices.
			- degree * num_vertices / 2 == whole number"""
		
		if degree < num_vertices and (degree * num_vertices)%2 == 0:
			return True
			
		else:
			return False


			

class CustomError(Exception):
	def __init__(self, value):
		self.value = value
		
	def __str__(self):
		return repr(self.value)		
		
		
				

def main(script, *args):

	v = Vertex('v')
	w = Vertex('w')
	x = Vertex('x')
	y = Vertex('y')
	
	vertices = [v, w, x, y]
	
	g = Graph(vertices)
	
# 	print g
	
	g.add_regular_edges(2)
	
	print g


#	 v = Vertex('v')
#	 print v
#	 w = Vertex('w')
#	 print w
#	 e = Edge(v, w)
#	 print e
#	 
#	 x = Vertex('x')
#	 
#	 f = Edge(v, x)
#	 
#	 h = Edge(w, x)
#	 
#	 print "Length of edge e is", e.get_length_of_edge()
#	 
#	 print "Vertices of e are", e.get_vertices()
#	 
#	 g = Graph([v,w], [e])
#	 g.add_vertex(x)
#	 g.add_edge(f)
#	 g.add_edge(h)
#	 
#	 print "Graph g is:", g
#	 
#	 print "Vertices connected with x are:", g.out_vertices(x)
#	 
#	 print "Edges connected with x are:", g.out_edges(x)
#	 
#	 
	
#	 print "Vertice 1 is", e.get_vertice(1)
#	 print "Vertice 2 is", e.get_vertice(2)
#	 
#	 f = Graph([v,w])
#	 print "Graph f is ", f
#	 
#	 g = Graph([v,w], [e])
#	 print g
#	 
#	 x = Vertex('x')
#	 y = Vertex('y')
#	 d = Edge(x, y)
#	 
#	 g.add_vertex(x)
#	 g.add_vertex(y)
#	 g.add_edge(d)
#	 
#	 edge_test = g.get_edge(v, w)
#	 print "Edge is", edge_test
#	 
#	 g.remove_edge(e)
#	 print "Graph is", g
#	 
#	 g.add_edge(e)
#	 print "Graph is", g
#	 
#	 print "Vertices of graph g are", g.vertices()
#	 
#	 print "Edges of graph g are", g.edges()


if __name__ == '__main__':
	import sys
	main(*sys.argv)