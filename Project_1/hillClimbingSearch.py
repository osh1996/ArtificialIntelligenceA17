
class hillClimbingSearch:

	def hillClimbingSearch(nodeObjects, startNode, goalNode):
		self.nodeObjects = nodeObjects
		self.startNode = getNode(startNode, nodeObjects)
		self.goalNode = getNode(startNode, nodeObjects)

		recursiveHillClimbing(self.startNode)

	def recursiveHillClimbing(self, node):
		if node.name == goalNode.name:
			return node
		else:
			nextNode = 0
			for edge in node.edges:
				child = edge[0]
				if nextNode is 0:
					nextNode = child
				else if child.heuristic < nextNode.heuristic:
					nextNode = child
				else if child.heuristic == nextNode.heuristic:			#tiebreak using alphabetical order of names
					if child.name < nextNode.name:
						nextNode = child
			recursiveHillClimbing(nextNode)