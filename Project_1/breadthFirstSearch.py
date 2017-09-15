from node import Node
from utility import printLabels
from generalSearch import generalSearch
from Queue import Queue
from queueItem import QueueItem

class breadthFirstSearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode


	def breadthFirstSearchFn(self):
		bfsQueue = Queue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, None, 0)
		initQueueTuple = (-1, startNodeQueueItem)
		bfsQueue.put_nowait(initQueueTuple)
		printLabels()

		result = generalSearch("breadth first", bfsQueue)
		return result

 