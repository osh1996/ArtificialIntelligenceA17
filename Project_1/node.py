class node:

	def __init__(self, name, heuristic):
		self.heuristic = heuristic
		self.name = name
		self.edges = set()
		
	def add_edge(self, node, cost):
		self.edges.add((node, cost))
