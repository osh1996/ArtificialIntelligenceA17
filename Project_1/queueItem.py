class QueueItem:
	
	def __init__(self, node, prevNode, pathCost):
		self.node = node
		self.prevNode = prevNode		## previous node in path as a queueItem
		self.pathCost = pathCost
		self.value = -1				## value of f(n), dependent on which
									## informed search algorithm is used
