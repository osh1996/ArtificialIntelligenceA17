class Node:

	def __init__(self, name, heuristic):
		self.name = name
		self.heuristic = heuristic
		self.edges = set()			#edges are tuples (node, length)

	def add_edge(self, node, cost):
		self.edges.add((node, cost))

	def get_edge(self, node):
		edges = list(self.edges)
		for edge in edges:
			if edge[0].name == node.name:
				return edge
		return -1


