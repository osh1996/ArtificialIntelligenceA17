from node import Node
from utility import getNode
from generalSearch import generalSearch
import Queue

class depthLimitSearch:

	#need to implement function for finding a node in nodeObjects given a name
	def depthLimitSearch(self, nodeObjects, startNode, goalNode, limit):
		self.nodeObjects = nodeObjects
		self.startNode = getNode(startNode, nodeObjects)
		self.goalNode = getNode(goalNode, nodeObjects)

		dlsQueue = LifoQueue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, null, 0)
		startNodeQueueItem.value = limit
		dlsQueue.put_nowait(startNodeQueueItem)

		generalSearch("depth limited", dlsQueue)


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

