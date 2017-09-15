class Path:
	
	def __init__(self, node, prevNode, pathCost):
		self.node = node
		self.prevNode = prevNode		## previous node in path as a path
		self.pathCost = pathCost
		self.fnValue = None

	def pathList(self):
		lis = list()
		while(prevNode.node):
			node = prevNode.node
			lis.append(node.name)
			node = prevNove.node
		return lis