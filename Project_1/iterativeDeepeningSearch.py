from node import Node
from utility import getNode
from generalSearch import generalSearch
import Queue
import depthLimitSearch

class iterativeDeepeningSearch:

	def __init__(self, startNode, goalNode):
		self.startNode = startNode
		self.goalNode = goalNode

	def iterativeDeepeningSearchFn(self)
		result = "start"
		for i in to_infinity():
			result = depthLimitSearch(self.nodeObjects, self.startNode, self.goalNode, i)
			if result == "G":
				return result
		if result == "fail" or result == "start":
			return "fail"
	
	def to_infinity(self):
    	index=0
    	while 1:
       		yield index
        	index += 1
