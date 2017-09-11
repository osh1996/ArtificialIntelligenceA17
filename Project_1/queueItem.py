class QueueItem:
	
	def __init__(self, node, prevNode, value):
		self.node = node
		self.prevNode = prevNode
		self.value = value			## value of f(n), dependent on which
									## informed search algorithm is used
