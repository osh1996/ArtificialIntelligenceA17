class node:

	def __init__(self, name):
		self.name = name
		self.edges = set()

	def add_heur(self, heur):
		self.heur = heur
	
	def add_edge(self, node, cost):
		self.edges.add((node, cost))
