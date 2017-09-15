from node import Node
from utility import printLabels
from queueItem import QueueItem
from Queue import PriorityQueue
from generalSearch import generalSearch

#just make a greedy choice each step based on the heuristic of each node

class aStarSearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode

	def aStarSearchFn(self):
		astarQueue = PriorityQueue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, None, 0)
		initQueueTuple = (startNodeQueueItem.node.heuristic, startNodeQueueItem)
		astarQueue.put_nowait(initQueueTuple)
		printLabels()

		generalSearch("astar", astarQueue)