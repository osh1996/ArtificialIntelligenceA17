from node import Node
from utility import getNode
from generalSearch import generalSearch
import Queue

class depthFirstSearch:

	def __init__(self, nodeObjects, startNode, goalNode):
		self.nodeObjects = nodeObjects
		self.startNode = startNode, nodeObjects
		self.goalNode = goalNode, nodeObjects


	def depthFirstSearchFn(self)
		dfsQueue = LifoQueue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, null, 0)
		initQueueTuple = (-1, startNodeQueueItem)
		dfsQueue.put_nowait(initQueueTuple)

		result = generalSearch("depth first", dfsQueue)
		return result


		




