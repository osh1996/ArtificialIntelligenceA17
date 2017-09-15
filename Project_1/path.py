class Path:
	
	def __init__(self, node, prevNode, pathCost):
		self.node = node
		self.prevNode = prevNode		## previous node in path as a queueItem
		self.pathCost = pathCost

	