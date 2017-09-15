class Path:
	
	def __init__(self, node, prevNode, pathCost):
		self.node = node
		self.prevNode = prevNode		## previous node in path as a path
		self.pathCost = pathCost
		self.fnValue = None

	