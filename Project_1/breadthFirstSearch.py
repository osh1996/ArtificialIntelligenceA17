from node import Node
import utility
from generalSearch import generalSearch
import Queue

class breadthFirstSearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode


	def breadthFirstSearchFn(self):
		bfsQueue = Queue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, -999, 0)
		initQueueTuple = (-1, startNodeQueueItem)
		bfsQueue.put_nowait(initQueueTuple)
		printLabels()

		result = generalSearch("breadth first", bfsQueue)
		return result

 