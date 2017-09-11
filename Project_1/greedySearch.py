from node import Node
import utility
from Queue import PriorityQueue
from generalSearch import generalSearch

#just make a greedy choice each step based on the heuristic of each node

class greedySearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode

	def greedySearchFn(self):
		greedyQueue = PriorityQueue(maxsize=0)
		startNodeQueueItem = QueueItem(self.startNode, null, 0)
		initQueueTuple = (startNodeQueueItem.node.heuristic, startNodeQueueItem)
		greedyQueue.put_nowait(initQueueTuple)
		printLabels()

		result = generalSearch("greedy", greedyQueue)
		return result
		


