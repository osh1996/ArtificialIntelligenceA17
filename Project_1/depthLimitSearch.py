from node import Node

class depthLimitSearch:

	#need to implement function for finding a node in nodeObjects given a name
	def depthLimitSearch(self, nodeObjects, startNode, goalNode, limit):
		self.nodeObjects = nodeObjects
		self.startNode = startNode
		self.goalNode = goalNode

		recurseDepthLimitSearch(self.startNode, limit)


	def recurseDepthLimitSearch(self, node, limit):
		limitHit = false
		if node.name == goalNode.name:
			return node
		else if limit == 0:
			return "limit hit"
		else:
			for edge in node.edges:
				child = edge[0]
				result = recurseDepthLimitSearch(child, limit-1)
				if result == "limit hit":
					limitHit = true
				else if result != failure:
					return result
			if limitHit:
				return "limit hit"
			else return "fail"

