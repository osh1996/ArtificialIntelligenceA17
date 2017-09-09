class node:

	def __init__(self, name, heuristic):
		self.heuristic = heuristic
		self.name = name
		self.edges = set()

	def add_edge(node, cost):
		self.edges.add((node, cost))
