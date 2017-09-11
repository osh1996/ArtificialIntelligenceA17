from node import Node
from utility import getNode
from generalSearch import generalSearch
import Queue

class depthLimitSearch:

	def __init__(self, startNode, goalNode, limit):
		self.startNode = startNode
		self.goalNode = goalNode
		self.limit = limit


	def depthLimitSearchFn(self)
		dlsQueue = LifoQueue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, null, 0)
		initQueueTuple = (self.limit, startNodeQueueItem)
		dlsQueue.put_nowait(initQueueTuple)

		result = generalSearch("depth limited", dlsQueue)
		return result


