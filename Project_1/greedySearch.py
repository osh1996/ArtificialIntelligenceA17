from node import Node
from utility import getNode

#just make a greedy choice each step based on the heuristic of each node

class greedySearch:

	def greedySearch(self, nodeObjects, startNode, goalNode):
		self.nodeObjects = nodeObjects
		self.startNode = getNode(startNode,nodeObjects)
		self.goalNode = getNode(goalNode,nodeObjects)

		recursiveGreedySearch(startNode)

	def recursiveGreedySearch(self, node):
		


