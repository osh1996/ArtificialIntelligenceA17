from node import Node
from utility import printLabels
from generalSearch import generalSearch
from Queue import LifoQueue
from queueItem import QueueItem

class depthFirstSearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode


	def depthFirstSearchFn(self):
		dfsQueue = LifoQueue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, None, 0)
		initQueueTuple = (-1, startNodeQueueItem)
		dfsQueue.put_nowait(initQueueTuple)
		printLabels()

		result = generalSearch("depth first", dfsQueue)
		return result


		




