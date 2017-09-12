from node import Node
from utility import printLabels
from generalSearch import generalSearch
from Queue import Queue
from queueItem import QueueItem

class uniformCostSearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode


	def uniformCostSearchFn(self):
		ucsQueue = Queue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, -999, 0)
		initQueueTuple = (0, startNodeQueueItem)
		ucsQueue.put_nowait(initQueueTuple)
		printLabels()

		result = generalSearch("uniform cost", ucsQueue)
		return result
					