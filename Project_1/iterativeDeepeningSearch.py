from node import Node
from utility import printLabelsIDS
from generalSearch import generalSearch
import Queue
import depthLimitSearch

class iterativeDeepeningSearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode

	def iterativeDeepeningSearchFn(self):
		result = "start"
		for i in range(0,100):
			result = depthLimitSearch.depthLimitSearch(self.startNode, self.goalNode, i)
			printLabelsIDS(i)
			if result == "G":
				return result
		if result == "fail" or result == "start":
			return "fail"
