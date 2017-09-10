
#just make a greedy choice each step based on the heuristic of each node

class greedySearch:

	def greedySearch(self, nodeObjects, startNode, goalNode):
		self.nodeObjects = nodeObjects
		self.startNode = startNode
		self.goalNode = goalNode

		recursiveGreedySearch(startNode)

	def recursiveGreedySearch(self, node):
		if node.name == goalNode.name:
			return node
		else:
			nextNode = 0
			for edge in node.edges:
				child = edge[0]
				if nextNode is 0:
					nextNode = child
				else if child.heuristic < nextNode


