class Node:

	def __init__(self, name, heuristic):
		self.name = name
		self.heuristic = heuristic
		self.edges = set()

	def add_edge(self, node, cost):
		self.edges.add((node, cost))


