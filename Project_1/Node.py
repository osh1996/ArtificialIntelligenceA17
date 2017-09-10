class Node:

	def __init__(self, name, heuristic):
		self.name = name
		self.heuristic = heuristic
		self.edges = set()

	def add_edge(self, node, cost):
		self.edges.add((node, cost))
	
	def get_Neigh(self, node):
		return self.node[edges]
	
	def get_cost(self, from_node, to_node):
		return self.heuristic[(from_node + to_node)]



