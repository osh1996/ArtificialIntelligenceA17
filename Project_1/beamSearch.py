from node import Node
from utility import getNode
from Queue import PriorityQueue
from generalSearch import generalSearch

#just make a greedy choice each step based on the heuristic of each node

class beamSearch:

	def __init__(self, nodeObjects, startNode, goalNode):
		self.nodeObjects = nodeObjects
		self.startNode = startNode
		self.goalNode = goalNode

	def beamSearchFn(self):
		beamQueue = PriorityQueue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, null, 0)
		initQueueTuple = (startNodeQueueItem.node.heuristic, startNodeQueueItem)
		beamQueue.put_nowait(initQueueTuple)

		result = generalSearch("beam", beamQueue)
		return result