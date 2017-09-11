from node import Node
from utility import getNode
from generalSearch import generalSearch
import Queue

class uniformCostSearch:

	def __init__(self, nodeObjects, startNode, goalNode):
		self.nodeObjects = nodeObjects
		self.startNode = startNode
		self.goalNode = goalNode


	def uniformCostSearchFn(self)
		ucsQueue = Queue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, null, 0)
		initQueueTuple = (0, startNodeQueueItem)
		ucsQueue.put_nowait(initQueueTuple)

		result = generalSearch("uniform cost", ucsQueue)
		return result
					