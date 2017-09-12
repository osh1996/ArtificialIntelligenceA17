from node import Node
from utility import printLabels
from Queue import PriorityQueue
from generalSearch import generalSearch
from queueItem import QueueItem

#just make a greedy choice each step based on the heuristic of each node

class greedySearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode

	def greedySearchFn(self):
		greedyQueue = PriorityQueue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, -999, 0)
		initQueueTuple = (startNodeQueueItem.node.heuristic, startNodeQueueItem)
		greedyQueue.put_nowait(initQueueTuple)
		printLabels()

		result = generalSearch("greedy", greedyQueue)
		return result
		


